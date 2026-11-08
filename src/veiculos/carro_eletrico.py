"""Carro elétrico: sedã branco com teto escuro, faixa turquesa na lateral, grade fechada e tampa de recarga
turquesa (sem escapamento)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402


def construir():
    V.carro('parede', comp=0.95, teto='escuro', hatch=False)
    for s in (-1, 1):
        L.caixa((0.012, 0.8, 0.025), (s * 0.211, 0, 0.13), 'agua')        # faixa turquesa
    L.caixa((0.18, 0.012, 0.04), (0, -0.48, 0.12), 'agua')                 # grade fechada
    L.caixa((0.012, 0.06, 0.05), (0.212, 0.3, 0.17), 'agua_funda')         # tampa de recarga


L.principal(__file__, construir)
