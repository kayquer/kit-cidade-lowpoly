"""Semáforo de pedestre: coluna baixa com grupo focal de duas luzes (vermelha em cima, verde embaixo) e
botoeira amarela na altura da mão."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.07, 0.03, (0, 0, 0), 'concreto', lados=8)
    L.cilindro(0.025, 0.85, (0, 0, 0.03), 'metal_escuro', lados=8)
    L.caixa((0.12, 0.08, 0.22), (0, -0.04, 0.66), 'escuro', chanfro=0.01)
    L.caixa((0.08, 0.012, 0.08), (0, -0.085, 0.77), 'vermelho')
    L.caixa((0.08, 0.012, 0.08), (0, -0.085, 0.68), 'verde')
    for z in (0.85, 0.76):
        L.caixa((0.1, 0.035, 0.008), (0, -0.095, z), 'escuro')                # palas
    L.caixa((0.07, 0.05, 0.1), (0, -0.04, 0.38), 'amarelo', chanfro=0.008)    # botoeira
    L.cilindro(0.015, 0.01, (0, -0.065, 0.42), 'escuro', lados=6, rot=(90, 0, 0))


L.principal(__file__, construir)
