"""Centro de Pesquisa (2×2): blocos de laboratório brancos com faixas de vidro, passarela coberta entre eles,
cúpula de observatório com fenda aberta, antena parabólica, torre de antenas, painéis solares e estacionamento."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def bloco(cx, cy, w, d, h, piso, andares=2):
    L.caixa((w, d, h), (cx, cy, piso), 'parede', chanfro=0.03)
    for i in range(andares):
        z = piso + 0.18 + i * (h - 0.1) / andares
        L.caixa((w + 0.02, d + 0.02, 0.16), (cx, cy, z), 'vidro')
    L.caixa((w + 0.06, d + 0.06, 0.06), (cx, cy, piso + h), 'metal')


def construir():
    L.caixa((4.0, 4.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.08
    L.caixa((3.7, 3.0, 0.05), (0, 0.35, piso), 'piso')
    piso += 0.05

    bloco(-0.85, 0.85, 1.8, 1.0, 1.0, piso)            # laboratório principal (fundo)
    bloco(1.1, 0.1, 1.0, 1.6, 0.75, piso, andares=1)    # laboratório baixo (direita)
    # Passarela coberta ligando os dois
    L.caixa((0.6, 0.35, 0.22), (0.35, 0.65, piso + 0.45), 'vidro', chanfro=0.01)
    L.caixa((0.64, 0.4, 0.04), (0.35, 0.65, piso + 0.67), 'metal')
    # Entrada principal com marquise
    L.placa(0.34, 0.36, (-0.85, 0.35, piso + 0.36), 'vidro_escuro', 'frente')
    L.caixa((0.7, 0.32, 0.04), (-0.85, 0.22, piso + 0.42), 'telhado_azul', chanfro=0.01)

    # Observatório: torre cilíndrica com cúpula e fenda
    ox, oy = -1.35, 0.85
    L.cilindro(0.36, 0.35, (ox, oy, piso + 1.0), 'parede', lados=12)
    L.cupula(0.38, (ox, oy, piso + 1.35), 'metal', lados=12, aneis=3)
    L.caixa((0.12, 0.42, 0.3), (ox, oy - 0.12, piso + 1.42), 'escuro', rot=(-30, 0, 0))   # fenda aberta
    L.cano((ox, oy - 0.1, piso + 1.45), (ox, oy - 0.38, piso + 1.62), 0.04, 'metal_escuro', lados=6)  # telescópio

    # Antena parabólica sobre o bloco baixo
    px, py, pz = 1.25, 0.45, piso + 0.81
    L.cilindro(0.04, 0.16, (px, py, pz), 'metal_escuro', lados=6)
    L.cupula(0.24, (px, py - 0.02, pz + 0.12), 'parede', lados=10, aneis=2)
    L.cano((px, py, pz + 0.18), (px, py - 0.1, pz + 0.38), 0.008, 'metal_escuro', lados=4)
    # Painéis solares no bloco principal
    for i in range(3):
        L.caixa((0.42, 0.3, 0.03), (-0.55 + i * 0.47, 1.05, piso + 1.08), 'painel_solar', rot=(-20, 0, 0))
    # Torre de antenas treliçada (fundo direito)
    tx, ty = 1.55, 1.55
    for (dx, dy) in ((-0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (0.1, 0.1)):
        L.cano((tx + dx, ty + dy, piso), (tx + dx * 0.25, ty + dy * 0.25, piso + 1.9), 0.012, 'vermelho', lados=4)
    for z in (0.5, 1.0, 1.5):
        f = 1 - z / 1.9 * 0.75
        L.caixa((0.2 * f + 0.02, 0.2 * f + 0.02, 0.02), (tx, ty, piso + z), 'parede')
    L.esfera(0.035, (tx, ty, piso + 1.93), 'vermelho')

    # Estacionamento na frente com dois carros simples
    L.caixa((1.6, 0.8, 0.008), (-0.75, -1.4, piso), 'asfalto')
    for i, cor in enumerate(('vermelho', 'telhado_azul')):
        x = -1.2 + i * 0.5
        L.caixa((0.28, 0.5, 0.12), (x, -1.4, piso + 0.04), cor, chanfro=0.02)
        L.caixa((0.24, 0.28, 0.1), (x, -1.38, piso + 0.16), 'vidro_escuro', chanfro=0.015)
    L.arvore((0.5, -1.4, piso), 0.75, 'verde')
    L.arvore((1.5, -1.45, piso), 0.65, 'verde_escuro')
    L.arbusto((-1.7, -0.5, piso), 0.14, 'folha')


L.principal(__file__, construir)
