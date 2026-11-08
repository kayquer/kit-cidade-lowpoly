"""Caminhão de bombeiros: cabine e carroceria vermelhas com faixa branca, compartimentos laterais de metal,
escada sobre o teto, mangueira enrolada, giroflex e três eixos de rodas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG = 0.5


def construir():
    V.chassi(LARG, -0.7, 0.75)
    V.cabine_caminhao('vermelho', LARG, y_frente=-0.78, comp=0.42, alt=0.42)
    L.caixa((0.28, 0.07, 0.04), (0, -0.62, 0.52), 'escuro')
    L.caixa((0.12, 0.065, 0.045), (-0.07, -0.62, 0.55), 'vermelho', chanfro=0.008)
    L.caixa((0.12, 0.065, 0.045), (0.07, -0.62, 0.55), 'telhado_azul', chanfro=0.008)
    L.caixa((LARG, 1.1, 0.38), (0, 0.21, 0.1), 'vermelho', chanfro=0.02)             # carroceria
    for s in (-1, 1):
        L.caixa((0.012, 1.08, 0.03), (s * (LARG / 2 + 0.002), 0.21, 0.42), 'parede')
        for yc in (-0.15, 0.13, 0.41):                                                   # compartimentos
            L.caixa((0.012, 0.24, 0.24), (s * (LARG / 2 + 0.003), yc, 0.14), 'metal')
            L.caixa((0.014, 0.08, 0.015), (s * (LARG / 2 + 0.005), yc, 0.25), 'metal_escuro')
    # Escada no teto: dois banzos e degraus
    for x in (-0.1, 0.1):
        L.caixa((0.025, 1.25, 0.025), (x, 0.1, 0.52), 'metal')
    for i in range(9):
        L.caixa((0.2, 0.015, 0.012), (0, -0.48 + i * 0.145, 0.53), 'metal')
    for x in (-0.1, 0.1):
        L.caixa((0.025, 0.025, 0.04), (x, 0.65, 0.48), 'metal_escuro')
    L.cilindro(0.07, 0.05, (-0.14, 0.62, 0.48), 'amarelo', lados=8)                   # mangueira enrolada
    V.lanternas(LARG, 0.76, 0.12)
    V.rodas(LARG, (-0.58, 0.4, 0.6), r=0.09)


L.principal(__file__, construir)
