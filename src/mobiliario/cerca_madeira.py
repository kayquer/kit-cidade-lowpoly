"""Cerca de madeira (trecho de 2 unidades ao longo de X): cinco mourões com ponta e duas travessas, para emendar
lado a lado na borda de um lote."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for i in range(5):
        x = -0.96 + i * 0.48
        L.caixa((0.05, 0.05, 0.3), (x, 0, 0), 'madeira_escura', chanfro=0.006)
        L.prisma([(-0.025, 0), (0.025, 0), (0, 0.04)], 0.05, (x, 0, 0.3), 'madeira_escura', eixo='Y')
    for z in (0.09, 0.21):
        L.caixa((2.0, 0.025, 0.05), (0, -0.035, z), 'madeira', chanfro=0.005)


L.principal(__file__, construir)
