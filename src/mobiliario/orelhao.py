"""Orelhão (telefone público brasileiro): concha laranja em forma de ovo com a abertura escura na frente,
aparelho cinza dentro, coluna e base de concreto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.08, 0.03, (0, 0, 0), 'concreto', lados=8)
    L.cilindro(0.025, 0.42, (0, 0.06, 0.03), 'metal_escuro', lados=6)
    # Concha: ovo laranja; a "boca" é um elipsoide escuro que aflora na frente
    L.esfera(0.2, (0, 0.03, 0.6), 'laranja', escala=(0.85, 0.8, 1.15), sub=2)
    L.esfera(0.2, (0, -0.05, 0.56), 'escuro', escala=(0.6, 0.55, 0.8), sub=2)   # forro interno
    L.caixa((0.07, 0.04, 0.11), (0, -0.14, 0.47), 'concreto', chanfro=0.008)   # aparelho
    L.caixa((0.025, 0.03, 0.08), (-0.048, -0.155, 0.49), 'metal_escuro')               # fone
    L.caixa((0.04, 0.01, 0.035), (0.008, -0.162, 0.54), 'escuro')         # teclado


L.principal(__file__, construir)
