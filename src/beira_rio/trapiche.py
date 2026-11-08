"""Trapiche (píer curto de madeira): sai de um pedaço de margem com grama (atrás, +Y) e avança sobre a água
(frente, -Y), com tábuas, estacas, cabeços de amarração com corda e um lampião na ponta."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.4, 1.6, 0.03), (0, -0.2, 0), 'agua')                       # água
    L.caixa((1.4, 0.45, 0.14), (0, 0.6, 0), 'terra', chanfro=0.015)        # margem
    L.caixa((1.4, 0.45, 0.03), (0, 0.6, 0.14), 'grama')
    # Estacas e vigas
    for y in (-0.85, -0.45, -0.05, 0.3):
        for x in (-0.22, 0.22):
            L.cilindro(0.03, 0.2, (x, y, 0.0), 'madeira_escura', lados=6)
    for x in (-0.22, 0.22):
        L.caixa((0.04, 1.3, 0.03), (x, -0.25, 0.17), 'madeira_escura')
    # Tábuas (deck), uma levemente mais escura a cada três
    for i in range(14):
        y = -0.88 + i * 0.09
        cor = 'madeira_escura' if i % 3 == 0 else 'madeira'
        L.caixa((0.56, 0.08, 0.02), (0, y, 0.2), cor)
    # Cabeços de amarração e corda
    for x in (-0.25, 0.25):
        L.cilindro(0.025, 0.08, (x, -0.8, 0.22), 'madeira_escura', lados=6)
    L.anel(0.035, 0.022, 0.02, (0.25, -0.8, 0.26), 'creme', lados=6)
    # Lampião
    L.caixa((0.04, 0.04, 0.42), (-0.25, -0.55, 0.22), 'madeira_escura')
    L.caixa((0.07, 0.07, 0.08), (-0.25, -0.55, 0.64), 'flor_amarela', chanfro=0.008)
    L.cone(0.065, 0.05, (-0.25, -0.55, 0.72), 'escuro', lados=4)


L.principal(__file__, construir)
