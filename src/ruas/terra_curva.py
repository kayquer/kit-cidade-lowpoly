"""Estrada de terra em curva (tile 2×2): liga -Y e +X num arco de 90° centrado no canto (+1, -1), mesma largura
do asfalto, com marcas de pneu e capim nas bordas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    cx, cy = 1, -1
    R.anel(cx, cy, 1 - R.MEIO, 1 + R.MEIO, 90, 180, 0, 0.02, 'terra', n=12)
    for r in (0.67, 1.33):                                     # trilhas dos pneus
        R.anel(cx, cy, r - 0.07, r + 0.07, 90, 180, 0.02, 0.024, 'composto', n=12)
    R.anel(cx, cy, 0.91, 1.09, 90, 180, 0.02, 0.026, 'verde_escuro', n=12)
    for (x, y, h) in ((0.85, -0.85, 0.1), (-0.6, 0.6, 0.12), (-0.85, 0.2, 0.09), (0.2, 0.85, 0.1), (0.55, -0.6, 0.08)):
        R.capim(x, y, h)


L.principal(__file__, construir)
