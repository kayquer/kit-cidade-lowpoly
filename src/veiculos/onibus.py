"""Ônibus urbano: carroceria branca longa com faixa verde, janelas contínuas, para-brisa grande, duas portas
no lado direito (+X), letreiro escuro sem texto, ar-condicionado no teto e duas rodas por lado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG, COMP = 0.5, 1.8


def construir():
    y0, y1 = -COMP / 2, COMP / 2
    L.caixa((LARG, COMP, 0.52), (0, 0, 0.08), 'parede', chanfro=0.03)
    # Faixas
    for s in (-1, 1):
        L.caixa((0.012, COMP - 0.06, 0.07), (s * (LARG / 2 + 0.002), 0, 0.15), 'verde')
        L.caixa((0.012, COMP - 0.06, 0.02), (s * (LARG / 2 + 0.002), 0, 0.24), 'amarelo')
    # Janelas laterais (lado esquerdo contínuo; no direito, entre as portas)
    L.caixa((0.012, COMP - 0.35, 0.17), (-(LARG / 2 + 0.003), 0.08, 0.38), 'vidro')
    for (ya, yb) in ((-0.62, 0.18), (0.42, 0.85)):
        L.caixa((0.012, yb - ya, 0.17), (LARG / 2 + 0.003, (ya + yb) / 2, 0.38), 'vidro')
    for yp in (-0.76, 0.3):                                     # portas (vidro escuro, até o chão)
        L.caixa((0.014, 0.2, 0.4), (LARG / 2 + 0.004, yp, 0.12), 'vidro_escuro')
        L.caixa((0.016, 0.01, 0.4), (LARG / 2 + 0.005, yp, 0.12), 'metal_escuro')
    # Frente e traseira
    L.caixa((LARG - 0.06, 0.012, 0.26), (0, y0 - 0.004, 0.3), 'vidro')
    L.caixa((LARG - 0.12, 0.014, 0.05), (0, y0 - 0.006, 0.535), 'escuro')     # letreiro
    L.caixa((LARG - 0.12, 0.012, 0.12), (0, y1 + 0.004, 0.42), 'vidro_escuro')
    L.caixa((LARG + 0.01, 0.04, 0.06), (0, y0 + 0.01, 0.07), 'escuro', chanfro=0.01)
    L.caixa((LARG + 0.01, 0.04, 0.06), (0, y1 - 0.01, 0.07), 'escuro', chanfro=0.01)
    V.farois(LARG, y0, 0.17)
    V.lanternas(LARG, y1, 0.17)
    L.caixa((0.3, 0.4, 0.06), (0, 0.25, 0.6), 'concreto', chanfro=0.015)    # ar-condicionado
    V.rodas(LARG, (y0 + 0.35, y1 - 0.38), r=0.1)


L.principal(__file__, construir)
