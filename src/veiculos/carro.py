"""Carro hatch vermelho: carroceria compacta, cabine de vidro com teto e coluna na cor, para-choques escuros,
faróis, lanternas e quatro rodas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402


def construir():
    V.carro('vermelho')
    L.caixa((0.03, 0.03, 0.02), (-0.2, -0.12, 0.29), 'escuro')   # retrovisores
    L.caixa((0.03, 0.03, 0.02), (0.2, -0.12, 0.29), 'escuro')


L.principal(__file__, construir)
