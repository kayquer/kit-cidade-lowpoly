"""Margem reta de rio (tile 2×2): metade -Y é água (como o tile agua), uma faixa de areia em degrau e a metade
+Y é grama na altura do terreno, com pedras e capim na beira."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    A = R.AREIA
    R.agua_fundo()
    L.caixa((2, 1, R.Z_AGUA - R.Z_LEITO), (0, -0.5, R.Z_LEITO), 'agua')
    L.caixa((2, A, R.Z_AREIA - R.Z_LEITO), (0, A / 2, R.Z_LEITO), 'areia')
    terra = 1 - A
    L.caixa((2, terra, -R.GRAMA - R.Z_LEITO), (0, A + terra / 2, R.Z_LEITO), 'terra')
    L.caixa((2, terra, R.GRAMA), (0, A + terra / 2, -R.GRAMA), 'grama')
    L.caixa((0.6, 0.03, 0.004), (-0.3, -0.45, R.Z_AGUA), 'agua_funda')
    for (x, y, r) in ((-0.55, 0.12, 0.06), (0.4, 0.08, 0.05)):
        L.esfera(r, (x, y, R.Z_AREIA), 'pedra', escala=(1.3, 1, 0.6))
    for (x, y) in ((-0.3, 0.3), (0.65, 0.28), (0.1, 0.35)):
        R.capim(x, y, 0.1)


L.principal(__file__, construir)
