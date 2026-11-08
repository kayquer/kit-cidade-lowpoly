"""Táxi: sedã amarelo com faixa laranja na lateral e luminoso branco e laranja no teto (sem texto)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402


def construir():
    V.carro('amarelo', comp=0.95, hatch=False)
    for s in (-1, 1):
        L.caixa((0.012, 0.75, 0.03), (s * 0.211, 0, 0.12), 'laranja')
    L.caixa((0.16, 0.07, 0.05), (0, 0.06, 0.38), 'parede', chanfro=0.01)   # luminoso
    L.caixa((0.165, 0.075, 0.015), (0, 0.06, 0.39), 'laranja')


L.principal(__file__, construir)
