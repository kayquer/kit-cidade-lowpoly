"""Poste de iluminação comum: base de concreto, coluna cônica cinza, braço curvo e luminária com lâmpada amarela."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.1, 0.08, (0, 0, 0), 'concreto', lados=8, r_topo=0.08, chanfro=0.01)
    L.cilindro(0.04, 1.5, (0, 0, 0.08), 'concreto_escuro', lados=8, r_topo=0.025)
    pts = [(0, 0, 1.55), (-0.08, 0, 1.66), (-0.22, 0, 1.7), (-0.4, 0, 1.68)]
    for a, b in zip(pts, pts[1:]):
        L.cano(a, b, 0.018, 'concreto_escuro', lados=6)
    L.caixa((0.2, 0.09, 0.05), (-0.44, 0, 1.63), 'metal_escuro', chanfro=0.01)
    L.caixa((0.16, 0.07, 0.012), (-0.44, 0, 1.625), 'flor_amarela')


L.principal(__file__, construir)
