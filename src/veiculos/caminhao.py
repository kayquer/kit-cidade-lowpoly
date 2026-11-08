"""Caminhão baú: cabine azul com para-brisa e janelas, baú creme com faixa azul e porta traseira com trincos,
chassi escuro, tanque lateral e três eixos de rodas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG = 0.5


def construir():
    V.chassi(LARG, -0.66, 0.7)
    V.cabine_caminhao('telhado_azul', LARG, y_frente=-0.7, comp=0.36)
    L.caixa((LARG, 0.98, 0.52), (0, 0.2, 0.11), 'creme', chanfro=0.02)          # baú
    for s in (-1, 1):
        L.caixa((0.012, 0.92, 0.05), (s * (LARG / 2 + 0.002), 0.2, 0.18), 'telhado_azul')
    L.caixa((LARG - 0.04, 0.012, 0.46), (0, 0.694, 0.14), 'concreto')            # porta traseira
    L.caixa((0.012, 0.014, 0.44), (0, 0.698, 0.15), 'metal_escuro')
    for x in (-0.08, 0.08):
        L.caixa((0.02, 0.016, 0.3), (x, 0.7, 0.2), 'metal_escuro')
    L.cilindro(0.045, 0.16, (-0.21, -0.3, 0.09), 'metal', lados=8, rot=(90, 0, 0))  # tanque
    V.lanternas(LARG, 0.69, 0.08)
    V.rodas(LARG, (-0.5, 0.35, 0.55), r=0.09)


L.principal(__file__, construir)
