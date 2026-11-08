"""Estacionamento (tile 2×2): pátio de asfalto aberto para a borda -Y, oito vagas pintadas de branco em duas
fileiras (uma vaga azul de acessibilidade), corredor no meio e calçada com meio-fio nas outras três bordas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    C, F, ZC = R.CALCADA, R.MEIO_FIO, R.Z_CALCADA
    interno = 1 - C                                   # 0.65: borda do pátio
    L.caixa((2 * interno, 1 + interno, R.Z_ASFALTO), (0, (interno - 1) / 2, 0), 'asfalto')
    # Calçadas em U (fundo +Y e laterais), com meio-fio
    L.caixa((2, C - F, ZC), (0, interno + F + (C - F) / 2, 0), 'piso')
    L.caixa((2 * interno + 2 * F, F, ZC + 0.005), (0, interno + F / 2, 0), 'concreto')
    for s in (-1, 1):
        L.caixa((C - F, 1 + interno, ZC), (s * (interno + F + (C - F) / 2), (interno - 1) / 2, 0), 'piso')
        L.caixa((F, 1 + interno, ZC + 0.005), (s * (interno + F / 2), (interno - 1) / 2, 0), 'concreto')
    # Vagas: 4 em cima (fundo) e 4 embaixo, separadas por linhas brancas
    larg = 2 * interno / 4
    z = R.Z_ASFALTO
    for fileira, (y0, y1) in enumerate(((0.12, interno), (-0.82, -0.3))):
        prof = y1 - y0
        for i in range(5):
            x = -interno + i * larg
            L.caixa((0.025, prof, 0.004), (x, (y0 + y1) / 2, z), 'parede')
        L.caixa((2 * interno, 0.025, 0.004), (0, y0 if fileira == 0 else y1, z), 'parede')
    L.caixa((larg - 0.08, interno - 0.16, 0.004), (-interno + larg / 2, (0.16 + interno) / 2, z), 'telhado_azul')
    # Seta do corredor (mão única) e uma árvore de sombra na calçada do fundo
    L.caixa((0.3, 0.035, 0.004), (0, -0.09, z), 'amarelo')
    L.prisma([(0.15, -0.16), (0.27, -0.09), (0.15, -0.02)], 0.004, (0, 0, z), 'amarelo', eixo='Z')
    L.arvore((0.82, 0.82, ZC), 0.7, 'verde')


L.principal(__file__, construir)
