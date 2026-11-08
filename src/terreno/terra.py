"""Terreno de terra batida (tile 2×2): bloco com o topo de terra, algumas pedrinhas e tufos de capim."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base('terra')
    L.caixa((0.5, 0.4, 0.004), (-0.4, 0.3, 0), 'composto')
    L.caixa((0.3, 0.5, 0.004), (0.5, -0.45, 0), 'composto')
    for (x, y, r) in ((0.3, 0.5, 0.04), (-0.55, -0.4, 0.05), (0.65, 0.2, 0.03)):
        L.esfera(r, (x, y, 0), 'pedra', escala=(1.2, 1, 0.6))
    for (x, y) in ((-0.75, 0.7), (0.75, -0.8), (0.1, -0.1)):
        R.capim(x, y, 0.08)


L.principal(__file__, construir)
