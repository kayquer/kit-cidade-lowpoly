"""Água (tile 2×2): leito de terra de z -0,3 a -0,2 e lâmina turquesa até z -0,12 (abaixo do nível do terreno,
então as peças de terra vizinhas viram barranco); duas ondinhas mais escuras."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.agua_fundo()
    L.caixa((2, 2, R.Z_AGUA - R.Z_LEITO), (0, 0, R.Z_LEITO), 'agua')
    for (x, y, c) in ((-0.4, 0.3, 0.5), (0.45, -0.5, 0.4)):
        L.caixa((c, 0.03, 0.004), (x, y, R.Z_AGUA), 'agua_funda')


L.principal(__file__, construir)
