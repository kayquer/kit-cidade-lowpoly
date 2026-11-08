"""Entroncamento em T de asfalto (tile 2×2): rua principal ligando -Y e +Y e um ramal para +X, com linha de
retenção e faixa de pedestres no ramal; calçada contínua do lado -X e cantos de calçada do lado +X."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    M, F, ZC = R.MEIO, R.MEIO_FIO, R.Z_CALCADA
    # Asfalto: cruz sem o braço -X
    L.caixa((2 * M, 2, R.Z_ASFALTO), (0, 0, 0), 'asfalto')
    L.caixa((1 - M, 2 * M, R.Z_ASFALTO), ((1 + M) / 2, 0, 0), 'asfalto')
    # Lado -X: calçada inteira com meio-fio
    L.caixa((R.CALCADA - F, 2, ZC), (-(M + F + (R.CALCADA - F) / 2), 0, 0), 'piso')
    L.caixa((F, 2, ZC + 0.005), (-(M + F / 2), 0, 0), 'concreto')
    # Lado +X: dois cantos de calçada com meio-fio em L
    for s in (-1, 1):
        yc = s * (M + 1) / 2
        L.caixa((1 - M - F, 1 - M - F, ZC), ((M + F + 1) / 2, s * (M + F + 1) / 2, 0), 'piso')
        L.caixa((F, 1 - M, ZC + 0.005), (M + F / 2, yc, 0), 'concreto')
        L.caixa((1 - M - F, F, ZC + 0.005), ((M + F + 1) / 2, s * (M + F / 2), 0), 'concreto')
    # Faixas: amarela tracejada na principal (interrompida no cruzamento), retenção e zebra no ramal
    R.tracos_y(-1, -M, 1)
    R.tracos_y(M, 1, 1)
    L.caixa((0.04, M - 0.05, 0.004), (M + 0.08, -M / 2 - 0.02, R.Z_ASFALTO), 'parede')   # linha de retenção
    R.zebra_x(0.86, larg=0.18)
    L.caixa((1 - M - 0.12, 0.04, 0.004), ((M + 1) / 2 + 0.06, 0, R.Z_ASFALTO), 'amarelo')


L.principal(__file__, construir)
