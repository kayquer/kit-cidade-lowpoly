"""Morro (tile 2×2): bloco alto com topo de grama em z 0,6, laterais em camadas (pedra embaixo, terra em cima),
duas pedras e um arbusto no topo."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402

TOPO = 0.6


def construir():
    L.caixa((2, 2, 0.2 - R.BASE), (0, 0, R.BASE), 'pedra')
    L.caixa((2, 2, TOPO - R.GRAMA - 0.2), (0, 0, 0.2), 'terra')
    L.caixa((2, 2, R.GRAMA), (0, 0, TOPO - R.GRAMA), 'grama')
    L.esfera(0.12, (-0.4, 0.35, TOPO), 'pedra', escala=(1.3, 1, 0.6))
    L.esfera(0.07, (-0.2, 0.5, TOPO), 'concreto_escuro', escala=(1.2, 1, 0.6))
    L.arbusto((0.45, -0.3, TOPO), 0.14, 'verde_escuro')
    R.capim(0.2, 0.6, 0.1, TOPO)


L.principal(__file__, construir)
