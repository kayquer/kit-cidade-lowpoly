"""Corpo de Bombeiros (1×1): quartel vermelho e branco com duas garagens de portões vermelhos, faixa branca,
sirene no telhado, torre de treino com janelas e mangueira pendurada, hidrante e cones na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'concreto', chanfro=0.02)
    piso = 0.08
    L.caixa((1.2, 0.6, 0.012), (-0.25, -0.6, piso), 'asfalto')            # pátio de saída das viaturas
    for x in (-0.55, 0.05):
        L.caixa((0.04, 0.5, 0.004), (x, -0.62, piso + 0.012), 'amarelo')   # faixas de saída

    # Quartel: corpo vermelho, faixa branca, platibanda
    bx, by, w, d, h = -0.25, 0.25, 1.35, 1.1, 0.85
    L.caixa((w, d, h), (bx, by, piso), 'vermelho', chanfro=0.025)
    L.caixa((w + 0.03, d + 0.03, 0.08), (bx, by, piso + 0.6), 'parede')
    L.caixa((w + 0.06, d + 0.06, 0.06), (bx, by, piso + h), 'parede')
    frente = by - d / 2
    # Duas garagens com portões vermelhos (com frisos) e moldura branca
    for gx in (-0.55, 0.05):
        L.placa(0.5, 0.52, (gx, frente, piso + 0.52), 'parede', 'frente', espessura=0.02)
        L.placa(0.44, 0.48, (gx, frente - 0.01, piso + 0.49), 'vermelho', 'frente', espessura=0.02)
        for i in range(4):
            L.placa(0.44, 0.015, (gx, frente - 0.025, piso + 0.12 + i * 0.1), 'escuro', 'frente', espessura=0.005)
    # Janelas do andar de cima e do lado direito
    L.janelas('frente', frente, piso + 0.73, bx - 0.5, bx + 0.5, 4, 0.16, 0.1)
    L.janelas('direita', bx + w / 2, piso + 0.35, by - 0.35, by + 0.35, 2, 0.2, 0.25, moldura='parede')
    # Sirene/giroflex no telhado
    L.cilindro(0.06, 0.05, (bx, by, piso + h + 0.06), 'metal_escuro', lados=6)
    L.cilindro(0.045, 0.06, (bx, by, piso + h + 0.11), 'vermelho', lados=6)

    # Torre de treino (direita, atrás)
    tx, ty = 0.7, 0.45
    L.caixa((0.42, 0.42, 1.6), (tx, ty, piso), 'creme', chanfro=0.02)
    L.caixa((0.48, 0.48, 0.06), (tx, ty, piso + 1.6), 'vermelho')
    for z in (0.45, 0.85, 1.25):
        L.placa(0.18, 0.2, (tx, ty - 0.21, piso + z + 0.1), 'escuro', 'frente')
        L.placa(0.18, 0.2, (tx + 0.21, ty, piso + z + 0.1), 'escuro', 'direita')
    L.cano((tx + 0.12, ty - 0.23, piso + 1.45), (tx + 0.12, ty - 0.23, piso + 0.5), 0.022, 'amarelo', lados=5)  # mangueira

    # Hidrante e cones
    L.cilindro(0.05, 0.16, (0.7, -0.7, piso), 'vermelho', lados=8)
    L.cupula(0.05, (0.7, -0.7, piso + 0.16), 'amarelo', lados=8, aneis=2)
    for (cx, cy) in ((0.35, -0.85), (0.5, -0.85)):
        L.cone(0.04, 0.12, (cx, cy, piso), 'laranja', lados=6)
    L.arbusto((-0.85, -0.85, piso), 0.12, 'verde')


L.principal(__file__, construir)
