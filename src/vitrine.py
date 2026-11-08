"""
Renders de vitrine do kit (EEVEE, câmera ortográfica isométrica, luz de dia, chão de grama):

    blender -b --factory-startup --python src/vitrine.py -- agua            # previews/agua.jpg (grade da categoria)
    blender -b --factory-startup --python src/vitrine.py -- agua --cada     # + previews/agua/<id>.jpg (uma por peça)
    blender -b --factory-startup --python src/vitrine.py -- tudo            # todas as categorias
    blender -b --factory-startup --python src/vitrine.py -- todos           # previews/todos.jpg (todas as peças numa grade)
    ... -- agua --blend saida.blend                                         # também salva a cena

Peças altas vão para o fundo; o enquadramento é calculado pelas caixas envolventes.
"""
import glob
import math
import os
import sys

import bpy
from mathutils import Vector

SRC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(SRC)
MODELOS = os.path.join(RAIZ, 'models')
PREVIEWS = os.path.join(RAIZ, 'previews')

args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
CADA = '--cada' in args
BLEND = args[args.index('--blend') + 1] if '--blend' in args else None
alvos = [a for a in args if not a.startswith('--') and a != BLEND] or ['tudo']
todas = sorted(d for d in os.listdir(MODELOS) if os.path.isdir(os.path.join(MODELOS, d)))
if 'tudo' in alvos:
    alvos = todas

DIRECAO = Vector((-0.42, 1.0, 0.82)).normalized()   # de onde a câmera olha (frente dos modelos = +Y após importar)


def cena_nova():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    cena = bpy.context.scene
    mundo = bpy.data.worlds.new('ceu')
    cena.world = mundo
    mundo.use_nodes = True
    bg = next(n for n in mundo.node_tree.nodes if n.type == 'BACKGROUND')
    bg.inputs['Color'].default_value = (0.55, 0.78, 0.95, 1)
    bg.inputs['Strength'].default_value = 0.9
    sol = bpy.data.objects.new('sol', bpy.data.lights.new('sol', 'SUN'))
    cena.collection.objects.link(sol)
    sol.data.energy = 3.2
    sol.data.color = (1.0, 0.95, 0.85)
    sol.data.angle = math.radians(6)
    sol.rotation_euler = (math.radians(50), 0, math.radians(-150))
    cam = bpy.data.objects.new('camera', bpy.data.cameras.new('camera'))
    cena.collection.objects.link(cam)
    cena.camera = cam
    cam.data.type = 'ORTHO'
    cam.rotation_euler = (-DIRECAO).to_track_quat('-Z', 'Y').to_euler()
    r = cena.render
    try:
        r.engine = 'BLENDER_EEVEE_NEXT'
    except TypeError:
        r.engine = 'BLENDER_EEVEE'
    cena.view_settings.view_transform = 'Standard'
    r.image_settings.file_format = 'JPEG'
    r.image_settings.quality = 88
    return cena


def importar(caminho, nome):
    antes = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=caminho)
    novos = [o for o in bpy.data.objects if o not in antes]
    pai = bpy.data.objects.new(nome, None)
    bpy.context.scene.collection.objects.link(pai)
    for o in novos:
        if o.parent is None:
            o.parent = pai
    bpy.context.view_layer.update()
    pts = [o.matrix_world @ Vector(c) for o in novos if o.type == 'MESH' for c in o.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return pai, lo, hi


def chao(cx, cy, sx, sy, espessura=0.4):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(cx, cy, -espessura / 2))
    ob = bpy.context.object
    ob.name = 'chao'
    ob.scale = (sx, sy, espessura)
    m = bpy.data.materials.new('grama')
    m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    b.inputs['Base Color'].default_value = (0.2, 0.55, 0.1, 1)
    b.inputs['Roughness'].default_value = 0.9
    ob.data.materials.append(m)
    mod = ob.modifiers.new('b', 'BEVEL')
    mod.width = min(0.05, espessura / 3)
    mod.segments = 1
    return ob


def enquadrar(cena, objetos, margem=1.08):
    """Centra a câmera ortográfica nas caixas envolventes dos objetos (no espaço da câmera)."""
    cam = cena.camera
    bpy.context.view_layer.update()
    rot = cam.rotation_euler.to_matrix()
    inv = rot.transposed()
    pts = []
    for o in objetos:
        for filho in [o] + list(o.children_recursive):
            if filho.type == 'MESH':
                pts += [inv @ (filho.matrix_world @ Vector(c)) for c in filho.bound_box]
    xs, ys, zs = [p.x for p in pts], [p.y for p in pts], [p.z for p in pts]
    centro = rot @ Vector(((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, max(zs) + 20))
    cam.location = centro
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    aspecto = cena.render.resolution_x / cena.render.resolution_y
    cam.data.ortho_scale = max(w, h * aspecto) * margem
    cam.data.clip_end = 200


def renderizar(cena, saida, res):
    cena.render.resolution_x, cena.render.resolution_y = res
    cena.render.filepath = saida
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    bpy.ops.render.render(write_still=True)
    print('VITRINE', saida)


def grade(arquivos, espaco=0.6):
    """Dispõe os modelos numa grade (altos ao fundo = -Y) e devolve os pais e a área ocupada."""
    itens = []
    for f in arquivos:
        pai, lo, hi = importar(f, os.path.basename(f)[:-4])
        itens.append((pai, lo, hi))
    itens.sort(key=lambda t: -(t[2].z - t[1].z))
    n = len(itens)
    colunas = max(1, round(math.sqrt(n * 1.7)))
    filas = [itens[i:i + colunas] for i in range(0, n, colunas)]
    y = 0.0
    larg_max = 0.0
    posicoes = []
    for fila in filas:
        prof = max(hi.y - lo.y for _, lo, hi in fila)
        larguras = [hi.x - lo.x for _, lo, hi in fila]
        total = sum(larguras) + espaco * (len(fila) - 1)
        larg_max = max(larg_max, total)
        x = -total / 2
        for (pai, lo, hi), lx in zip(fila, larguras):
            pai.location = (x - lo.x, y + prof / 2 - (lo.y + hi.y) / 2, -lo.z)
            posicoes.append(pai)
            x += lx + espaco
        y += prof + espaco
    # y cresce para +Y (perto da câmera); as primeiras filas (altas) ficam no fundo
    for pai in posicoes:
        pai.location.y -= y / 2
    return posicoes, larg_max + 1.0, y + 0.6


for alvo in alvos:
    if alvo == 'todos':
        arquivos = sorted(glob.glob(os.path.join(MODELOS, '*', '*.glb')))
        saida = os.path.join(PREVIEWS, 'todos.jpg')
        res = (2400, 1350)
    else:
        arquivos = sorted(glob.glob(os.path.join(MODELOS, alvo, '*.glb')))
        saida = os.path.join(PREVIEWS, alvo + '.jpg')
        res = (1920, 1080)
    if not arquivos:
        print('SEM MODELOS', alvo)
        continue
    cena = cena_nova()
    pais, sx, sy = grade(arquivos)
    chao(0, 0, sx, sy)
    enquadrar(cena, pais + [bpy.data.objects['chao']], margem=1.04)
    if BLEND:
        bpy.ops.wm.save_as_mainfile(filepath=BLEND)
    renderizar(cena, saida, res)

    if CADA and alvo != 'todos':
        for f in arquivos:
            cena = cena_nova()
            pai, lo, hi = importar(f, os.path.basename(f)[:-4])
            pai.location = (-(lo.x + hi.x) / 2, -(lo.y + hi.y) / 2, -lo.z)
            folga = 0.12 * max(hi.x - lo.x, hi.y - lo.y) + 0.04
            base = chao(0, 0, hi.x - lo.x + folga, hi.y - lo.y + folga, espessura=min(0.3, folga * 0.6))
            enquadrar(cena, [pai], margem=1.12)   # enquadra a peça; a base pode sair um pouco do quadro
            renderizar(cena, os.path.join(PREVIEWS, alvo, os.path.basename(f)[:-4] + '.jpg'), (480, 360))
