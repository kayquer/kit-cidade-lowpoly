"""Floreira de concreto de calçada: caixa quadrada com terra, arbusto central e flores rosas e amarelas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.tanque(0.46, 0.46, 0.24, (0, 0, 0), cor_agua='terra', cor='concreto', parede=0.05, nivel=0.03, chanfro=0.012)
    L.arbusto((0, 0.02, 0.21), 0.15, 'verde')
    L.arbusto((0.12, -0.1, 0.21), 0.08, 'verde_escuro')
    L.arbusto((-0.12, -0.1, 0.21), 0.08, 'folha')
    for (x, y, z, cor) in ((0.05, -0.1, 0.36, 'flor_rosa'), (-0.07, 0.03, 0.38, 'flor_amarela'),
                           (0.12, -0.12, 0.3, 'flor_amarela'), (-0.13, -0.12, 0.3, 'flor_rosa')):
        L.esfera(0.024, (x, y, z), cor)


L.principal(__file__, construir)
