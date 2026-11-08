"""Ponte de concreto (tile 2×2, substitui um tile de água): leito e água iguais ao tile `agua` e, por cima, o
tabuleiro ligando -Y e +Y na altura da rua (asfalto, faixa amarela, calçadas e meio-fio), vigas laterais,
guarda-corpo com postes e dois pilares com sapata descendo até o leito."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    # Água (igual ao tile agua)
    R.agua_fundo()
    L.caixa((2, 2, R.Z_AGUA - R.Z_LEITO), (0, 0, R.Z_LEITO), 'agua')
    # Tabuleiro: laje de concreto por baixo do perfil de rua
    L.caixa((2, 2, 0.06), (0, 0, -0.06), 'concreto')
    R.rua_y()
    for s in (-1, 1):
        L.caixa((0.06, 2, 0.1), (s * 0.97, 0, -0.1), 'concreto_escuro')          # viga lateral
        # Guarda-corpo: corrimão e postes
        L.caixa((0.035, 2, 0.03), (s * 0.965, 0, R.Z_CALCADA + 0.17), 'metal')
        L.caixa((0.02, 2, 0.015), (s * 0.965, 0, R.Z_CALCADA + 0.08), 'metal')
        for i in range(5):
            L.caixa((0.04, 0.04, 0.2), (s * 0.965, -0.8 + i * 0.4, R.Z_CALCADA), 'metal_escuro')
    # Pilares (um par no meio) com sapata no leito
    for x in (-0.55, 0.55):
        L.caixa((0.22, 0.22, 0.04), (x, 0, R.Z_LEITO), 'concreto_escuro')
        L.cilindro(0.08, -0.06 - R.Z_LEITO - 0.04, (x, 0, R.Z_LEITO + 0.04), 'concreto', lados=8)
    L.caixa((1.5, 0.16, 0.05), (0, 0, -0.11), 'concreto_escuro')                 # travessa sobre os pilares


L.principal(__file__, construir)
