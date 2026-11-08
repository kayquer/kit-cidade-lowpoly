"""
Cena de exemplo: um bairro montado só com peças do kit (ruas e terreno modulares, prédios, rio com ponte,
veículos, mobiliário e vegetação). Serve de capa do README e de exemplo de como encaixar as peças.

    blender -b --factory-startup --python src/cena_cidade.py -- [saida.jpg] [--blend cena.blend]

Grade: célula (cx, cy) = lote 2 × 2 com centro em (2·cx, 2·cy). `rot` é o giro em graus (anti-horário, visto de
cima) a partir da orientação de autoria dos scripts: prédios e veículos com a frente para -Y; asfalto_reta liga
-Y/+Y; asfalto_curva liga -Y/+X; asfalto_t liga -Y/+Y/+X; asfalto_ponta só -Y; margem_reta tem a água em -Y.
O .glb volta do glTF girado 180°, por isso cada peça recebe 180° + rot ao ser colocada.
"""
import math
import os
import sys

import bpy
from mathutils import Matrix, Vector

SRC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(SRC)
MODELOS = os.path.join(RAIZ, 'models')
args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
BLEND = args[args.index('--blend') + 1] if '--blend' in args else None
livres = [a for a in args if not a.startswith('--') and a != BLEND]
SAIDA = livres[0] if livres else os.path.join(RAIZ, 'previews', 'capa.jpg')

W, H = 12, 14                 # colunas × linhas de lotes
RUAS_X = (1, 4, 7)            # linhas com rua ao longo de X
RUAS_Y = (4, 8)               # colunas com rua ao longo de Y (a de cx 8 termina em T na linha 7)
RIO = 9                       # linha da água; margens em 8 e 10

pecas = []                    # (nome, x, y, rot)


def por(nome, cx, cy, rot=0, dx=0.0, dy=0.0):
    """Coloca um modelo com centro na célula (cx, cy) (aceita meio-lote para prédios N × N) + deslocamento."""
    pecas.append((nome, 2 * cx + dx, 2 * cy + dy, rot))


def predio(nome, cx, cy, n=1, rot=0):
    """Prédio N × N com o canto inferior-esquerdo na célula (cx, cy)."""
    por(nome, cx + (n - 1) / 2, cy + (n - 1) / 2, rot)
    for i in range(n):
        for j in range(n):
            ocupado.add((cx + i, cy + j))


ocupado = set()

# --- Ruas, rio e margens -------------------------------------------------------------------------------
for cy in range(H):
    for cx in range(W):
        rua_x, rua_y = cy in RUAS_X, cx in RUAS_Y and not (cx == 8 and cy > 7)
        if cx == 4 and cy == RIO:
            por('ruas/ponte', cx, cy)
        elif cx == 4 and cy == H - 1:
            por('ruas/asfalto_ponta', cx, cy)
        elif rua_x and rua_y:
            if cx == 8 and cy == 7:
                por('ruas/asfalto_t', cx, cy, -90)       # liga -Y, -X e +X
            else:
                por('ruas/asfalto_cruzamento', cx, cy)
        elif rua_y and cy not in (RIO,):
            faixa = cy in (2, 5) and cx == 8
            por('ruas/asfalto_faixa_pedestre' if faixa else 'ruas/asfalto_reta', cx, cy)
        elif rua_x:
            faixa = cx in (3, 5) and cy == 4
            por('ruas/asfalto_faixa_pedestre' if faixa else 'ruas/asfalto_reta', cx, cy, 90)
        elif cy == RIO:
            por('terreno/agua', cx, cy)
        elif cy == RIO - 1:
            por('terreno/margem_reta', cx, cy, 180)    # água para +Y
        elif cy == RIO + 1:
            por('terreno/margem_reta', cx, cy)         # água para -Y
        else:
            continue
        ocupado.add((cx, cy))

# --- Quadras ----------------------------------------------------------------------------------------
for i, nome in enumerate(['casa_simples', 'casa_sobrado', 'casas_geminadas', 'predio_apartamentos']):
    predio('residencial/' + nome, i, 2)
for i, nome in enumerate(['residencial/casas_geminadas', 'residencial/predio_alto', 'comercial/hotel', 'comercial/escritorio']):
    predio(nome, i, 3)
for i, nome in enumerate(['comercial/loja_esquina', 'comercial/mercado', 'comercial/restaurante']):
    predio(nome, 5 + i, 2)
for i, nome in enumerate(['comercial/banco', 'publicos/posto_saude', 'publicos/policia']):
    predio(nome, 5 + i, 3)
for i, nome in enumerate(['publicos/bombeiros', 'comercial/posto_recarga', 'publicos/centro_tecnologia']):
    predio(nome, 9 + i, 2)
for i, nome in enumerate(['publicos/biblioteca', 'industrial/galpao', 'industrial/oficina']):
    predio(nome, 9 + i, 3)

predio('publicos/escola', 0, 5, 2)
predio('publicos/prefeitura', 2, 5, 2)
predio('comercial/shopping', 5, 5, 2)
predio('agua/caixa_dagua', 7, 5)
predio('residuos/ponto_coleta', 7, 6)
predio('publicos/hospital', 9, 5, 2)
predio('residencial/predio_apartamentos', 11, 5)
predio('residencial/casa_sobrado', 11, 6)

predio('agua/eta', 0, 11, 2)
predio('agua/ete', 2, 11, 2)
predio('energia/usina_solar', 5, 11, 3)
predio('energia/parque_eolico', 9, 11, 2)

# --- Terreno livre: grama, mata e decoração ------------------------------------------------------------
decor = {
    (0, 0): [('terreno/arvores_mata', 0, 0, 0)],
    (1, 0): [('vegetacao/ipe_amarelo', 0, 0, 0)],
    (2, 0): [('ruas/praca', 0, 0, 0)],
    (3, 0): [('mobiliario/parquinho', 0, 0, 0)],
    (5, 0): [('mobiliario/quiosque', -0.4, 0, 0), ('mobiliario/banco_praca', 0.5, -0.3, 0)],
    (6, 0): [('vegetacao/horta', -0.3, 0.2, 0), ('vegetacao/composteira', 0.4, -0.5, 0)],
    (7, 0): [('vegetacao/araucaria', 0, 0.2, 0), ('vegetacao/arbustos', 0.5, -0.5, 0)],
    (9, 0): [('mobiliario/ponto_onibus', 0, 0.45, 0), ('mobiliario/lixeira_seletiva', -0.5, -0.4, 0)],
    (10, 0): [('terreno/arvores_mata', 0, 0, 0)],
    (11, 0): [('vegetacao/ipe_amarelo', 0, 0, 0)],
    (11, 12): [('terreno/arvores_mata', 0, 0, 0)],
    (11, 11): [('vegetacao/araucaria', 0, 0, 0)],
    (0, 13): [('terreno/arvores_mata', 0, 0, 0)],
    (1, 13): [('vegetacao/araucaria', 0, 0, 0)],
    (2, 13): [('terreno/arvores_mata', 0, 0, 0)],
    (3, 13): [('vegetacao/ipe_amarelo', 0, 0, 0)],
    (8, 13): [('terreno/arvores_mata', 0, 0, 0)],
    (9, 13): [('terreno/arvores_mata', 0, 0, 0)],
    (10, 13): [('vegetacao/araucaria', 0, 0, 0)],
    (11, 13): [('terreno/arvores_mata', 0, 0, 0)],
    (8, 11): [('vegetacao/arbustos', 0, 0, 0)],
    (8, 12): [('vegetacao/pedras', 0, 0, 0)],
}
for cy in range(H):
    for cx in range(W):
        if (cx, cy) in ocupado:
            continue
        itens = decor.get((cx, cy), [])
        if not any(n.startswith(('terreno/', 'ruas/')) for n, *_ in itens):
            por('terreno/grama', cx, cy)
        for nome, dx, dy, rot in itens:
            por(nome, cx, cy, rot, dx, dy)

# --- Rio: barcos, bichos e beira ---------------------------------------------------------------------
por('beira_rio/canoa', 1, RIO, 80)
por('beira_rio/boia_rio', 6, RIO, 0)
por('beira_rio/barco_pesca', 9, RIO, -70, 0.2)
por('beira_rio/trapiche', 10, RIO + 1, 0, 0, -0.6)
por('beira_rio/garca', 2, RIO - 1, 30, 0.3, 0.3)
por('beira_rio/capivara', 7, RIO + 1, -30, 0, -0.3)
por('vegetacao/buriti', 11, RIO - 1, 0, 0.3, 0.2)
por('vegetacao/pedras', 0, RIO + 1, 0, 0.2, 0.2)
por('mobiliario/placa_educativa', 3, RIO + 1, 0, 0.3, 0.45)

# --- Veículos (mão inglesa não: no Brasil anda-se pela direita) ---------------------------------------
FAIXA = 0.33
por('veiculos/carro', 2, 1, 90, 0, -FAIXA)            # indo para +X
por('veiculos/taxi', 6, 1, -90, 0, FAIXA)             # indo para -X
por('veiculos/onibus', 10, 4, 90, 0, -FAIXA)
por('veiculos/caminhao_lixo', 1, 4, -90, 0, FAIXA)
por('veiculos/ambulancia', 8, 3, 180, FAIXA, 0)       # indo para +Y
por('veiculos/carro_eletrico', 4, 5, 0, -FAIXA, 0)    # indo para -Y
por('veiculos/caminhao_pipa', 4, RIO + 1, 0, -FAIXA, 0)
por('veiculos/caminhao_bombeiros', 6, 7, 90, 0, -FAIXA)
por('veiculos/carro', 10, 7, -90, 0, FAIXA)

# --- Mobiliário nas calçadas ----------------------------------------------------------------------------
CAL = 0.83
for cx in (1, 6, 10):
    por('mobiliario/poste_luz', cx, 1, 0, 0, CAL)
    por('mobiliario/poste_luz', cx, 4, 0, 0, -CAL)
por('mobiliario/semaforo', 4, 1, 0, CAL, -CAL)
por('mobiliario/semaforo', 8, 4, 180, -CAL, CAL)
por('mobiliario/hidrante', 2, 4, 0, 0.5, CAL)
por('mobiliario/lixeira', 6, 4, 0, 0.4, CAL)
por('mobiliario/orelhao', 10, 1, 0, 0.5, CAL)
por('mobiliario/placa_pare', 8, 7, 0, CAL, -CAL)
por('mobiliario/poste_solar', 2, 7, 0, 0, CAL)
por('mobiliario/poste_solar', 6, 7, 0, 0, CAL)

# --- Montagem ------------------------------------------------------------------------------------------
bpy.ops.wm.read_factory_settings(use_empty=True)
cena = bpy.context.scene
modelos = {}
for nome, x, y, rot in pecas:
    if nome not in modelos:
        antes = set(bpy.data.objects)
        bpy.ops.import_scene.gltf(filepath=os.path.join(MODELOS, nome + '.glb'))
        novos = [o for o in bpy.data.objects if o not in antes]
        bpy.context.view_layer.update()
        modelos[nome] = [(o.data, o.matrix_world.copy()) for o in novos if o.type == 'MESH']
        for o in novos:
            bpy.data.objects.remove(o)
    giro = Matrix.Translation((x, y, 0)) @ Matrix.Rotation(math.radians(180 + rot), 4, 'Z')
    for malha, m in modelos[nome]:
        ob = bpy.data.objects.new(nome.split('/')[1], malha)   # malha compartilhada (instância leve)
        cena.collection.objects.link(ob)
        ob.matrix_world = giro @ m

# Bloco de terra embaixo de tudo (a lateral do terreno)
bpy.ops.mesh.primitive_cube_add(size=1, location=(W - 1, H - 1, -0.55))
base = bpy.context.object
base.scale = (2 * W, 2 * H, 0.5)
mat = bpy.data.materials.new('terra')
mat.use_nodes = True
bsdf = next(n for n in mat.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
bsdf.inputs['Base Color'].default_value = (0.25, 0.15, 0.08, 1)
base.data.materials.append(mat)

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
sol.rotation_euler = (math.radians(48), 0, math.radians(35))

# Câmera isométrica vinda de -Y/+X: vê a frente (-Y) e o lado direito (+X) dos prédios
direcao = Vector((0.62, -1.0, 0.95)).normalized()
cam = bpy.data.objects.new('camera', bpy.data.cameras.new('camera'))
cena.collection.objects.link(cam)
cena.camera = cam
cam.data.type = 'ORTHO'
cam.rotation_euler = (-direcao).to_track_quat('-Z', 'Y').to_euler()
bpy.context.view_layer.update()
rot = cam.rotation_euler.to_matrix()
inv = rot.transposed()
pts = [inv @ Vector((x, y, z)) for x in (-1, 2 * W - 1) for y in (-1, 2 * H - 1) for z in (-0.8, 2.5)]
xs, ys, zs = [p.x for p in pts], [p.y for p in pts], [p.z for p in pts]
cam.location = rot @ Vector(((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, max(zs) + 40))
r = cena.render
r.resolution_x, r.resolution_y = 2400, 1350
cam.data.ortho_scale = max(max(xs) - min(xs), (max(ys) - min(ys)) * r.resolution_x / r.resolution_y) * 1.02
cam.data.clip_end = 300
try:
    r.engine = 'BLENDER_EEVEE_NEXT'
except TypeError:
    r.engine = 'BLENDER_EEVEE'
try:
    cena.eevee.use_shadows = True
except AttributeError:
    pass
cena.view_settings.view_transform = 'Standard'
r.image_settings.file_format = 'JPEG'
r.image_settings.quality = 90
r.filepath = SAIDA
if BLEND:
    bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)
print('CENA', SAIDA, len(pecas), 'peças')
