"""Estrada de terra reta (tile 2×2): liga -Y e +Y com a mesma largura do asfalto (1,3), sem calçada; marcas de
pneu mais escuras, capim nas bordas e algumas pedrinhas, sobre o bloco de grama."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    L.caixa((2 * R.MEIO, 2, 0.02), (0, 0, 0), 'terra')
    for x in (-0.33, 0.33):                                    # trilhas dos pneus
        L.caixa((0.14, 2, 0.004), (x, 0, 0.02), 'composto')
    L.caixa((0.18, 2, 0.006), (0, 0, 0.02), 'verde_escuro')    # capim no meio
    for (x, y, h) in ((-0.75, -0.6, 0.1), (0.78, -0.1, 0.12), (-0.8, 0.45, 0.09), (0.72, 0.7, 0.1)):
        R.capim(x, y, h)
    for (x, y) in ((0.5, -0.4), (-0.15, 0.6)):
        L.esfera(0.035, (x, y, 0.02), 'pedra', escala=(1.2, 1, 0.6))


L.principal(__file__, construir)
