"""Garça-branca em pé numa pedra da beira do rio: corpo branco, pescoço em S, bico amarelo apontado para a
frente (-Y) e pernas finas escuras."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.2, 0.012, (0, 0, 0), 'agua', lados=10)
    L.esfera(0.11, (0, 0.03, 0.04), 'pedra', escala=(1.2, 1, 0.6))
    z0 = 0.09
    for x in (-0.025, 0.025):                                           # pernas
        L.cano((x, 0.03, z0), (x, 0.04, z0 + 0.2), 0.006, 'escuro', lados=4)
    L.esfera(0.07, (0, 0.06, z0 + 0.26), 'parede', escala=(0.8, 1.35, 0.8))      # corpo
    L.cone(0.05, 0.1, (0, 0.17, z0 + 0.22), 'parede', lados=5)                    # cauda (aponta para cima)
    pts = [(0, -0.02, z0 + 0.3), (0, -0.05, z0 + 0.38), (0, -0.02, z0 + 0.45), (0, -0.04, z0 + 0.52)]
    for a, b in zip(pts, pts[1:]):
        L.cano(a, b, 0.018, 'parede', lados=5)
    L.esfera(0.03, (0, -0.05, z0 + 0.53), 'parede', escala=(0.9, 1.2, 0.9))       # cabeça
    L.cilindro(0.012, 0.09, (0, -0.07, z0 + 0.53), 'amarelo', lados=4, r_topo=0.0, rot=(90, 0, 0))
    for x in (-0.02, 0.02):
        L.esfera(0.006, (x, -0.06, z0 + 0.54), 'escuro')


L.principal(__file__, construir)
