"""Bicicleta solta: quadro verde-turquesa, rodas finas com cubo, selim, guidão e cestinha na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for py in (-0.2, 0.2):
        L.cilindro(0.11, 0.015, (-0.0075, py, 0.11), 'escuro', lados=12, rot=(0, 90, 0))
        L.cilindro(0.025, 0.02, (-0.01, py, 0.11), 'metal', lados=6, rot=(0, 90, 0))
    a, b, c = (0, 0.2, 0.11), (0, 0.0, 0.11), (0, 0.02, 0.29)     # traseira, pedal, canote
    d = (0, -0.17, 0.3)                                            # caixa de direção
    for p, q in ((a, c), (b, c), (a, b), (c, d), (b, d), (d, (0, -0.2, 0.11))):
        L.cano(p, q, 0.009, 'agua_funda', lados=5)
    L.caixa((0.04, 0.08, 0.015), (0, 0.03, 0.3), 'escuro')                               # selim
    L.cano((0, -0.17, 0.3), (0, -0.16, 0.35), 0.008, 'metal', lados=5)
    L.cano((-0.08, -0.16, 0.35), (0.08, -0.16, 0.35), 0.008, 'escuro', lados=5)          # guidão
    L.caixa((0.09, 0.07, 0.06), (0, -0.22, 0.25), 'madeira', chanfro=0.006)             # cestinha
    L.cilindro(0.012, 0.01, (-0.01, 0.0, 0.11), 'metal_escuro', lados=6, rot=(0, 90, 0))  # pedal


L.principal(__file__, construir)
