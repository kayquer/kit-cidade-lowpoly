"""Centro de Tecnologia (1×1): prédio moderno de vidro em três volumes escalonados com montantes metálicos,
telhado coberto de painéis solares, torre de antena, entrada com pé-direito duplo e jardim com bancos."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def volume(cx, cy, w, d, h, piso):
    """Caixa de vidro com laje clara em cima e montantes nas duas faces visíveis."""
    L.caixa((w, d, h), (cx, cy, piso), 'vidro', chanfro=0.015)
    L.caixa((w + 0.05, d + 0.05, 0.06), (cx, cy, piso + h), 'parede')
    for i in range(1, 4):
        z = piso + h * i / 4
        L.caixa((w + 0.02, d + 0.02, 0.025), (cx, cy, z), 'metal')
    for i in range(1, 4):
        x = cx - w / 2 + w * i / 4
        L.caixa((0.025, 0.02, h), (x, cy - d / 2 - 0.005, piso), 'metal')
        y = cy - d / 2 + d * i / 4
        L.caixa((0.02, 0.025, h), (cx + w / 2 + 0.005, y, piso), 'metal')
    return piso + h + 0.06


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.14
    L.caixa((1.9, 1.9, 0.06), (0, 0, 0.08), 'piso')

    # Três volumes escalonados (o mais alto atrás)
    volume(-0.05, 0.45, 1.3, 0.9, 1.7, piso)
    topo = volume(0.35, -0.15, 0.9, 0.7, 0.9, piso)
    L.caixa((0.5, 0.35, 0.5), (-0.5, -0.25, piso), 'vidro_escuro', chanfro=0.015)   # átrio da entrada
    L.caixa((0.56, 0.4, 0.05), (-0.5, -0.25, piso + 0.5), 'parede')
    L.placa(0.2, 0.32, (-0.5, -0.43, piso + 0.32), 'metal_escuro', 'frente')

    # Painéis solares nos telhados e torre de antena
    for i in range(2):
        L.caixa((0.36, 0.26, 0.025), (0.17 + i * 0.38, -0.15, topo + 0.06), 'painel_solar', rot=(-18, 0, 0))
    ztopo = piso + 1.76
    for i in range(3):
        L.caixa((0.36, 0.26, 0.025), (-0.45 + i * 0.4, 0.3, ztopo + 0.06), 'painel_solar', rot=(-18, 0, 0))
    L.cano((0.4, 0.7, ztopo), (0.4, 0.7, ztopo + 0.7), 0.015, 'metal', lados=4)
    L.cano((0.3, 0.7, ztopo + 0.5), (0.5, 0.7, ztopo + 0.5), 0.008, 'metal', lados=4)
    L.esfera(0.03, (0.4, 0.7, ztopo + 0.72), 'vermelho')
    L.cupula(0.1, (-0.4, 0.75, ztopo), 'parede', lados=8, aneis=2)          # radome

    # Jardim com bancos na frente
    L.caixa((0.6, 0.3, 0.08), (0.45, -0.75, piso), 'madeira')
    L.arbusto((0.3, -0.75, piso + 0.08), 0.1, 'verde')
    L.arbusto((0.55, -0.75, piso + 0.08), 0.1, 'folha')
    L.caixa((0.35, 0.09, 0.07), (-0.2, -0.78, piso), 'madeira')
    L.arvore((-0.8, -0.75, piso), 0.6, 'verde')


L.principal(__file__, construir)
