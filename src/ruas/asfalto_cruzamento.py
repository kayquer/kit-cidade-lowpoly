"""Cruzamento de asfalto (tile 2×2): liga as quatro bordas; faixas de pedestres zebradas nos quatro braços e
quatro cantos de calçada com meio-fio em L."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    M, F, ZC = R.MEIO, R.MEIO_FIO, R.Z_CALCADA
    L.caixa((2 * M, 2, R.Z_ASFALTO), (0, 0, 0), 'asfalto')
    for s in (-1, 1):
        L.caixa((1 - M, 2 * M, R.Z_ASFALTO), (s * (1 + M) / 2, 0, 0), 'asfalto')
    for sx in (-1, 1):
        for sy in (-1, 1):
            L.caixa((1 - M - F, 1 - M - F, ZC), (sx * (M + F + 1) / 2, sy * (M + F + 1) / 2, 0), 'piso')
            L.caixa((F, 1 - M, ZC + 0.005), (sx * (M + F / 2), sy * (M + 1) / 2, 0), 'concreto')
            L.caixa((1 - M - F, F, ZC + 0.005), (sx * (M + F + 1) / 2, sy * (M + F / 2), 0), 'concreto')
    for s in (-1, 1):
        R.zebra_y(s * 0.84, larg=0.2)
        R.zebra_x(s * 0.84, larg=0.2)


L.principal(__file__, construir)
