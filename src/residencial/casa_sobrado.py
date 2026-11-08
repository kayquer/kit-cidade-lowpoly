"""Sobrado (1×1): casa de dois andares azul-clara e branca, telhado de quatro águas, sacada com guarda-corpo
no andar de cima, garagem com portão de enrolar na lateral, entrada de carro e canteiro na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.08
    L.caixa((0.6, 0.9, 0.015), (0.55, -0.48, piso), 'concreto')           # entrada de carro
    L.caixa((0.22, 0.6, 0.015), (-0.25, -0.62, piso), 'piso')             # caminho
    # Corpo principal (dois andares)
    cx, cy, larg, prof = -0.25, 0.2, 1.0, 0.95
    L.caixa((larg, prof, 0.55), (cx, cy, piso), 'parede', chanfro=0.02)
    L.caixa((larg, prof, 0.55), (cx, cy, piso + 0.55), 'agua', chanfro=0.02)
    L.caixa((larg + 0.04, prof + 0.04, 0.04), (cx, cy, piso + 0.55), 'parede')    # faixa entre andares
    L.telhado4(larg, prof, 0.35, (cx, cy, piso + 1.1), 'telhado_vermelho', beiral=0.08)
    frente = cy - prof / 2
    L.placa(0.2, 0.38, (-0.25, frente, piso + 0.19), 'madeira_escura', 'frente')
    L.janelas('frente', frente, piso + 0.32, -0.62, -0.47, 1, 0.18, 0.22, moldura='parede')
    L.janelas('frente', frente, piso + 0.32, -0.03, 0.12, 1, 0.16, 0.22, moldura='parede')
    L.janelas('direita', cx + larg / 2, piso + 0.82, cy - 0.3, cy + 0.3, 2, 0.18, 0.22, moldura='parede')
    # Sacada no andar de cima: porta de vidro, laje, guarda-corpo
    L.placa(0.42, 0.34, (-0.3, frente, piso + 0.78), 'vidro', 'frente')
    L.caixa((0.62, 0.26, 0.04), (-0.3, frente - 0.13, piso + 0.57), 'parede')
    L.caixa((0.62, 0.02, 0.15), (-0.3, frente - 0.25, piso + 0.61), 'vidro')
    L.caixa((0.62, 0.025, 0.02), (-0.3, frente - 0.25, piso + 0.76), 'metal')
    # Garagem lateral térrea com laje e portão
    gx = 0.55
    L.caixa((0.6, 0.85, 0.48), (gx, cy - 0.05, piso), 'parede', chanfro=0.015)
    L.caixa((0.66, 0.9, 0.05), (gx, cy - 0.05, piso + 0.48), 'concreto_escuro')
    L.placa(0.48, 0.36, (gx, cy - 0.475, piso + 0.19), 'metal', 'frente')
    for i in range(4):
        L.placa(0.48, 0.012, (gx, cy - 0.49, piso + 0.06 + i * 0.09), 'metal_escuro', 'frente', espessura=0.01)
    L.janelas('direita', gx + 0.3, piso + 0.3, cy - 0.2, cy + 0.2, 1, 0.2, 0.15, moldura='parede')
    # Vasos na laje da garagem e canteiro
    L.arbusto((gx + 0.15, cy + 0.2, piso + 0.53), 0.09, 'verde')
    L.caixa((0.5, 0.18, 0.08), (-0.6, -0.72, piso), 'madeira')
    L.arbusto((-0.7, -0.72, piso + 0.08), 0.1, 'verde')
    L.arbusto((-0.5, -0.72, piso + 0.08), 0.09, 'folha')
    L.esfera(0.025, (-0.55, -0.79, piso + 0.17), 'flor_amarela')


L.principal(__file__, construir)
