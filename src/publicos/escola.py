"""Escola (2×2): prédio de dois andares em L com faixa laranja e telhado de telha, quadra poliesportiva coberta
com arquibancada, pátio calçado com bancos e árvore, mastro com bandeira e portão de entrada na frente."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def ala(cx, cy, w, d, piso, h=1.1):
    """Bloco de dois andares com faixa laranja entre os andares e telhado de quatro águas."""
    L.caixa((w, d, h), (cx, cy, piso), 'parede', chanfro=0.03)
    L.caixa((w + 0.03, d + 0.03, 0.08), (cx, cy, piso + 0.5), 'laranja')
    L.caixa((w + 0.06, d + 0.06, 0.06), (cx, cy, piso + h), 'creme')
    L.telhado4(w, d, 0.35, (cx, cy, piso + h + 0.06), 'telhado_vermelho', beiral=0.08)


def construir():
    L.caixa((4.0, 4.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.14
    L.caixa((3.8, 3.8, 0.06), (0, 0, 0.08), 'piso')

    # Prédio em L: ala do fundo (ao longo de X) e ala da esquerda (ao longo de Y)
    ala(-0.45, 1.2, 2.7, 0.95, piso)
    ala(-1.3, -0.15, 1.0, 1.75, piso)
    # Janelas: frente da ala do fundo, frente e lado direito da ala da esquerda (dois andares)
    for z in (piso + 0.3, piso + 0.82):
        L.janelas('frente', 1.2 - 0.475, z, -0.75, 0.85, 4, 0.24, 0.24, moldura='creme')
        L.janelas('frente', -0.15 - 0.875, z, -1.7, -0.9, 2, 0.22, 0.24, moldura='creme')
        L.janelas('direita', -1.3 + 0.5, z, -0.95, 0.55, 3, 0.24, 0.24, moldura='creme')
    L.janelas('direita', -0.45 + 1.35, piso + 0.82, 0.9, 1.5, 2, 0.2, 0.24, moldura='creme')
    # Porta principal com marquise azul na quina do L
    L.placa(0.36, 0.42, (-0.55, 1.2 - 0.475, piso + 0.42), 'madeira_escura', 'frente')
    L.caixa((0.6, 0.3, 0.04), (-0.55, 1.2 - 0.6, piso + 0.48), 'telhado_azul', chanfro=0.01)
    # Relógio na ala do fundo
    L.cilindro(0.12, 0.03, (0.45, 1.2 - 0.49, piso + 0.82), 'parede', lados=10, rot=(90, 0, 0))
    L.caixa((0.02, 0.02, 0.08), (0.45, 1.2 - 0.51, piso + 0.82), 'escuro')

    # Quadra coberta (frente direita): piso verde com linhas, pilares e cobertura em arco
    qx, qy, qw, qd = 0.85, -0.55, 1.9, 1.7
    L.caixa((qw, qd, 0.03), (qx, qy, piso), 'telhado_verde')
    L.caixa((qw - 0.2, 0.025, 0.005), (qx, qy, piso + 0.03), 'parede')                     # linha do meio
    L.anel(0.22, 0.2, 0.005, (qx, qy, piso + 0.03), 'parede', lados=10)                    # círculo central
    for dy in (-1, 1):
        L.caixa((qw - 0.2, 0.025, 0.005), (qx, qy + dy * (qd / 2 - 0.1), piso + 0.03), 'parede')
        L.cano((qx - 0.1, qy + dy * (qd / 2 - 0.18), piso), (qx - 0.1, qy + dy * (qd / 2 - 0.18), piso + 0.3),
               0.012, 'metal', lados=4)                                                     # traves
        L.cano((qx + 0.1, qy + dy * (qd / 2 - 0.18), piso), (qx + 0.1, qy + dy * (qd / 2 - 0.18), piso + 0.3),
               0.012, 'metal', lados=4)
        L.cano((qx - 0.1, qy + dy * (qd / 2 - 0.18), piso + 0.3), (qx + 0.1, qy + dy * (qd / 2 - 0.18), piso + 0.3),
               0.012, 'metal', lados=4)
    for px in (qx - qw / 2 + 0.05, qx + qw / 2 - 0.05):
        for py in (qy - qd / 2 + 0.05, qy, qy + qd / 2 - 0.05):
            L.caixa((0.06, 0.06, 0.75), (px, py, piso), 'metal_escuro')
    arco = []
    n = 6
    for i in range(n + 1):
        a = math.pi * i / n
        arco.append((-(qw / 2 + 0.05) * math.cos(a), 0.3 * math.sin(a)))
    interno = [(x * 0.97, z * 0.85) for (x, z) in reversed(arco)]
    L.prisma(arco + interno, qd + 0.1, (qx, qy, piso + 0.75), 'telhado_azul', eixo='Y')
    # Arquibancada de concreto no lado de fora da quadra (direita)
    for i in range(2):
        L.caixa((0.14, 1.2, 0.08 * (i + 1)), (qx + qw / 2 - 0.2 + i * 0.14 + 0.25, qy, piso), 'concreto')

    # Pátio: bancos, árvore e mastro com bandeira
    for bx in (-0.35, -0.0):
        L.caixa((0.28, 0.1, 0.08), (bx, 0.25, piso), 'madeira')
    L.arvore((-0.25, -0.35, piso), 0.8, 'verde')
    L.cano((-1.7, -1.6, piso), (-1.7, -1.6, piso + 1.5), 0.02, 'metal', lados=5)
    L.caixa((0.04, 0.4, 0.26), (-1.7, -1.4, piso + 1.2), 'telhado_azul')
    L.esfera(0.05, (-1.7, -1.4, piso + 1.33), 'parede', escala=(0.3, 1, 1))

    # Muro baixo e portão na frente
    L.caixa((1.5, 0.06, 0.18), (-1.15, -1.85, piso), 'creme')
    L.caixa((0.06, 0.06, 0.32), (-0.37, -1.85, piso), 'creme')
    L.caixa((0.06, 0.06, 0.32), (-0.03, -1.85, piso), 'creme')
    L.caixa((0.28, 0.03, 0.22), (-0.2, -1.85, piso), 'verde', chanfro=0.005)


L.principal(__file__, construir)
