"""Terreno de areia (tile 2×2): bloco com o topo de areia clara, uma concha e dois tufos de capim-da-praia."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base('areia')
    L.cupula(0.04, (0.4, -0.3, 0), 'creme', lados=6, aneis=2)
    for (x, y) in ((-0.6, 0.5), (0.7, 0.65)):
        R.capim(x, y, 0.09)
    L.esfera(0.05, (-0.3, -0.6, 0), 'pedra', escala=(1.3, 1, 0.5))


L.principal(__file__, construir)
