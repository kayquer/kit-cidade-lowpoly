"""Fábrica (2×2): galpão de tijolo com telhado em dente de serra (sheds com vidro virado para o fundo),
escritório anexo, chaminé alta com filtro e faixas, tanques, doca de carga com caminhão e pátio de asfalto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def caminhao(x, y, z):
    """Caminhão baú simples de frente para -Y."""
    for wy in (-0.35, -0.05, 0.25):
        for wx in (-0.17, 0.17):
            L.cilindro(0.075, 0.06, (x + wx + (0.03 if wx > 0 else -0.03), y + wy, z + 0.075), 'escuro', lados=8,
                       rot=(0, 90, 0))
    L.caixa((0.36, 0.3, 0.3), (x, y - 0.38, z + 0.06), 'telhado_azul', chanfro=0.02)     # cabine
    L.caixa((0.33, 0.04, 0.12), (x, y - 0.53, z + 0.22), 'vidro_escuro')
    L.caixa((0.4, 0.75, 0.42), (x, y + 0.15, z + 0.08), 'parede', chanfro=0.02)          # baú
    L.caixa((0.41, 0.6, 0.06), (x, y + 0.15, z + 0.3), 'laranja')


def construir():
    L.caixa((4.0, 4.0, 0.06), (0, 0, 0), 'concreto', chanfro=0.02)
    piso = 0.06
    L.caixa((1.6, 1.4, 0.01), (0.95, -1.15, piso), 'asfalto')                    # pátio de carga

    # Galpão principal com telhado em dente de serra (4 sheds)
    gx, gy, w, d, h = -0.35, 0.55, 2.9, 2.2, 0.9
    L.caixa((w, d, h), (gx, gy, piso), 'telhado_vermelho', chanfro=0.025)        # tijolo
    L.caixa((w + 0.03, d + 0.03, 0.08), (gx, gy, piso + 0.12), 'concreto_escuro')
    n = 4
    passo = d / n
    for i in range(n):
        y0 = gy - d / 2 + i * passo
        # perfil (y, z): sobe devagar do lado da frente e cai na vertical (vidro) virado para +Y
        L.prisma([(0, 0), (passo, 0), (passo, 0.42)], w, (gx, y0, piso + h), 'metal', eixo='X')
        L.caixa((w - 0.1, 0.03, 0.36), (gx, y0 + passo - 0.02, piso + h), 'vidro')
    # Janelas altas e portões
    L.janelas('frente', gy - d / 2, piso + 0.6, gx - 1.3, gx + 0.3, 4, 0.26, 0.2, moldura='concreto')
    L.janelas('direita', gx + w / 2, piso + 0.6, gy - 0.9, gy + 0.9, 4, 0.26, 0.2, moldura='concreto')
    L.placa(0.6, 0.6, (gx + 1.0, gy - d / 2, piso + 0.6), 'metal_escuro', 'frente')
    for i in range(5):
        L.placa(0.6, 0.015, (gx + 1.0, gy - d / 2 - 0.02, piso + 0.08 + i * 0.12), 'metal', 'frente', espessura=0.005)
    # Doca de carga
    L.caixa((0.9, 0.35, 0.18), (gx + 1.0, gy - d / 2 - 0.17, piso), 'concreto')
    L.caixa((0.9, 0.04, 0.18), (gx + 1.0, gy - d / 2 - 0.35, piso), 'amarelo')

    # Escritório anexo (frente esquerda)
    L.caixa((1.0, 0.55, 0.6), (-1.2, -0.85, piso), 'parede', chanfro=0.02)
    L.caixa((1.05, 0.6, 0.05), (-1.2, -0.85, piso + 0.6), 'concreto_escuro')
    L.janelas('frente', -1.125, piso + 0.38, -1.6, -0.8, 3, 0.18, 0.18)
    L.placa(0.2, 0.32, (-0.95, -1.125, piso + 0.32), 'vidro_escuro', 'frente')

    # Chaminé com faixas e filtro no topo
    cx, cy = 1.5, 1.45
    L.cilindro(0.2, 2.6, (cx, cy, piso), 'concreto', lados=10, r_topo=0.14)
    for z in (2.0, 2.35):
        L.cilindro(0.165, 0.1, (cx, cy, piso + z), 'vermelho', lados=10)
    L.cilindro(0.18, 0.18, (cx, cy, piso + 2.6), 'metal_escuro', lados=10)        # filtro
    L.cano((cx - 0.3, cy, piso + 0.7), (cx - 0.1, cy, piso + 0.7), 0.05, 'metal', lados=6)
    # Tanques e caminhão
    for (tx, ty) in ((1.55, 0.55), (1.55, 0.05)):
        L.cilindro(0.2, 0.75, (tx, ty, piso), 'metal', lados=10, chanfro=0.01)
        L.cupula(0.2, (tx, ty, piso + 0.75), 'metal', lados=10, aneis=2)
    caminhao(0.65, -1.15, piso)
    L.arvore((-1.6, -1.55, piso), 0.6, 'verde')


L.principal(__file__, construir)
