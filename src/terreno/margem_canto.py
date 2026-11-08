"""Margem em canto (tile 2×2): água num quarto de círculo de raio 1 centrado no canto (-1, -1), faixa de areia
em degrau acompanhando a curva e grama no resto; casa com a margem_reta nas bordas -X e -Y."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    A = R.AREIA
    c = (-1, -1)
    R.agua_fundo()
    R.poligono([c] + R.arco(-1, -1, 1, 0, 90, 10), R.Z_LEITO, R.Z_AGUA, 'agua')
    R.anel(-1, -1, 1, 1 + A, 0, 90, R.Z_LEITO, R.Z_AREIA, 'areia', n=10)
    fora = R.arco(-1, -1, 1 + A, 90, 0, 10)                   # de (-1, 0.18) até (0.18, -1)
    contorno = fora + [(1, -1), (1, 1), (-1, 1)]
    R.poligono(contorno, R.Z_LEITO, -R.GRAMA, 'terra')
    R.poligono(contorno, -R.GRAMA, 0, 'grama')
    L.esfera(0.06, (-0.05, -0.15, R.Z_AREIA), 'pedra', escala=(1.3, 1, 0.6))
    for (x, y) in ((0.25, 0.1), (-0.3, 0.4), (0.5, -0.5)):
        R.capim(x, y, 0.1)
    L.arbusto((0.6, 0.6, 0), 0.12, 'verde')


L.principal(__file__, construir)
