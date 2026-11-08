"""Ambulância (furgão): carroceria branca alta com capô curto, faixas vermelhas, para-brisa, porta traseira dupla,
giroflex vermelho e azul no teto (sem símbolos nem texto)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG, COMP = 0.46, 1.1


def construir():
    y0, y1 = -COMP / 2, COMP / 2
    L.caixa((LARG, 0.2, 0.18), (0, y0 + 0.1, 0.08), 'parede', chanfro=0.03)          # capô
    L.caixa((LARG, COMP - 0.18, 0.46), (0, 0.09, 0.08), 'parede', chanfro=0.03)       # baú
    L.caixa((LARG - 0.06, 0.012, 0.15), (0, y0 + 0.174, 0.31), 'vidro')                 # para-brisa
    for s in (-1, 1):
        L.caixa((0.012, 0.16, 0.13), (s * (LARG / 2 + 0.003), y0 + 0.3, 0.32), 'vidro')
        L.caixa((0.012, COMP - 0.06, 0.05), (s * (LARG / 2 + 0.002), 0.0, 0.2), 'vermelho')
        L.caixa((0.012, COMP - 0.3, 0.02), (s * (LARG / 2 + 0.002), 0.12, 0.27), 'vermelho')
    L.caixa((LARG - 0.04, 0.012, 0.4), (0, y1 + 0.004, 0.1), 'concreto')               # porta traseira
    L.caixa((0.01, 0.014, 0.4), (0, y1 + 0.006, 0.1), 'metal_escuro')
    L.caixa((LARG - 0.12, 0.014, 0.12), (0, y1 + 0.006, 0.34), 'vidro_escuro')
    L.caixa((LARG + 0.01, 0.04, 0.05), (0, y0 + 0.01, 0.06), 'escuro', chanfro=0.01)
    V.farois(LARG, y0, 0.18)
    V.lanternas(LARG, y1, 0.2)
    L.caixa((0.3, 0.07, 0.04), (0, y0 + 0.24, 0.54), 'escuro')                        # giroflex
    L.caixa((0.13, 0.065, 0.045), (-0.075, y0 + 0.24, 0.57), 'vermelho', chanfro=0.008)
    L.caixa((0.13, 0.065, 0.045), (0.075, y0 + 0.24, 0.57), 'telhado_azul', chanfro=0.008)
    V.rodas(LARG, (y0 + 0.22, y1 - 0.22))


L.principal(__file__, construir)
