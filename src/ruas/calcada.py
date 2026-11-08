"""Calçada (tile 2×2): lote todo calçado na altura da calçada das ruas (0,07), com juntas das placas em grade."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    L.caixa((2, 2, R.Z_CALCADA), (0, 0, 0), 'piso')
    for i in (-0.5, 0, 0.5):
        L.caixa((0.015, 2, 0.003), (i, 0, R.Z_CALCADA), 'concreto_escuro')
        L.caixa((2, 0.015, 0.003), (0, i, R.Z_CALCADA), 'concreto_escuro')


L.principal(__file__, construir)
