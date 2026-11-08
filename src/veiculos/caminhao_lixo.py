"""Caminhão de lixo (coletor compactador): cabine branca, caçamba verde arredondada com faixa amarela,
compactador traseiro inclinado com boca escura, estribos para os garis e luz giratória laranja."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG = 0.5


def construir():
    V.chassi(LARG, -0.66, 0.66)
    V.cabine_caminhao('parede', LARG, y_frente=-0.7, comp=0.36)
    L.cilindro(0.025, 0.03, (0, -0.42, 0.56), 'laranja', lados=6)                 # giroflex
    # Caçamba: caixa com teto arredondado (cilindro deitado ao longo de Y)
    L.caixa((LARG, 0.8, 0.36), (0, 0.06, 0.11), 'verde', chanfro=0.02)
    L.cilindro(LARG / 2, 0.8, (0, 0.46, 0.47), 'verde', lados=10, rot=(90, 0, 0))
    for s in (-1, 1):
        L.caixa((0.012, 0.76, 0.04), (s * (LARG / 2 + 0.002), 0.06, 0.2), 'amarelo')
    # Compactador traseiro: perfil inclinado (y, z) extrudado em X
    perfil = [(0.46, 0.0), (0.72, 0.0), (0.68, 0.5), (0.46, 0.6)]
    L.prisma(perfil, LARG - 0.02, (0, 0, 0.1), 'metal_escuro', eixo='X')
    L.prisma([(0.7, 0.02), (0.72, 0.02), (0.69, 0.3), (0.67, 0.3)], LARG - 0.1, (0, 0.003, 0.1), 'escuro', eixo='X')
    for s in (-1, 1):                                                               # estribos e alças
        L.caixa((0.12, 0.06, 0.015), (s * 0.17, 0.75, 0.08), 'metal')
        L.cano((s * 0.2, 0.71, 0.2), (s * 0.2, 0.69, 0.45), 0.008, 'metal', lados=4)
    V.lanternas(LARG, 0.72, 0.12)
    V.rodas(LARG, (-0.5, 0.4), r=0.09)


L.principal(__file__, construir)
