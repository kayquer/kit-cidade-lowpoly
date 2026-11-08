"""Lixeira comum de calçada (papeleira): cesto laranja com borda escura preso num poste baixo de metal."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.06, 0.02, (0, 0.06, 0), 'concreto', lados=6)
    L.cilindro(0.018, 0.48, (0, 0.06, 0.02), 'metal_escuro', lados=6)
    L.caixa((0.04, 0.04, 0.04), (0, 0.035, 0.36), 'metal_escuro')                  # suporte
    L.cilindro(0.095, 0.22, (0, -0.04, 0.2), 'laranja', lados=10, r_topo=0.105, chanfro=0.008)
    L.anel(0.11, 0.09, 0.02, (0, -0.04, 0.41), 'escuro', lados=10)
    L.cilindro(0.088, 0.005, (0, -0.04, 0.405), 'escuro', lados=10)               # boca


L.principal(__file__, construir)
