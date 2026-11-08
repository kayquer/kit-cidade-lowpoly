"""Praça (tile 2×2): piso de pedra portuguesa clara com caminho em cruz, quatro canteiros de grama nos cantos
com arbustos e flores, uma árvore em cada canteiro do fundo e bancos voltados para o centro."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    L.caixa((2, 2, R.Z_CALCADA), (0, 0, 0), 'creme')
    L.caixa((0.36, 2, 0.003), (0, 0, R.Z_CALCADA), 'parede')          # caminho em cruz
    L.caixa((2, 0.36, 0.003), (0, 0, R.Z_CALCADA), 'parede')
    L.cilindro(0.22, 0.004, (0, 0, R.Z_CALCADA), 'pedra', lados=10)    # rosa central
    z = R.Z_CALCADA
    for sx in (-1, 1):
        for sy in (-1, 1):
            cx, cy = sx * 0.58, sy * 0.58
            L.caixa((0.64, 0.64, 0.06), (cx, cy, z), 'concreto')
            L.caixa((0.58, 0.58, 0.065), (cx, cy, z), 'grama')
            if sy > 0:
                L.arvore((cx + sx * 0.05, cy + 0.05, z + 0.065), 0.9, 'verde' if sx < 0 else 'verde_escuro')
            else:
                L.arbusto((cx + sx * 0.12, cy - 0.1, z + 0.065), 0.1, 'verde_escuro')
                L.arbusto((cx - sx * 0.12, cy + 0.08, z + 0.065), 0.09, 'folha')
                L.esfera(0.025, (cx, cy - 0.05, z + 0.13), 'flor_rosa')
                L.esfera(0.025, (cx - sx * 0.1, cy + 0.15, z + 0.12), 'flor_amarela')
    # Dois bancos na beira do caminho, um de cada lado
    for (x, y) in ((-0.55, 0.13), (0.55, -0.13)):
        L.caixa((0.3, 0.09, 0.02), (x, y, z + 0.09), 'madeira')
        for d in (-0.11, 0.11):
            L.caixa((0.025, 0.08, 0.09), (x + d, y, z), 'escuro')


L.principal(__file__, construir)
