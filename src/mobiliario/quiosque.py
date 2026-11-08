"""Quiosque de praça: base octogonal, corpo verde com balcão de madeira e janela de atendimento na frente,
cobertura cônica vermelha com beiral, toldo listrado e dois banquinhos."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.45, 0.04, (0, 0, 0), 'concreto', lados=8, chanfro=0.01)
    L.cilindro(0.34, 0.62, (0, 0, 0.04), 'verde', lados=8, chanfro=0.01)
    # Janela de atendimento (frente) e balcão
    L.caixa((0.36, 0.05, 0.22), (0, -0.31, 0.34), 'escuro')
    L.caixa((0.42, 0.12, 0.03), (0, -0.35, 0.33), 'madeira', chanfro=0.006)
    L.caixa((0.3, 0.03, 0.06), (0, -0.31, 0.4), 'flor_amarela')            # produtos na vitrine
    # Toldo listrado sobre a janela
    for i in range(5):
        cor = 'parede' if i % 2 else 'vermelho'
        L.caixa((0.09, 0.16, 0.012), (-0.18 + i * 0.09, -0.4, 0.6), cor, rot=(-18, 0, 0))
    # Cobertura
    L.cilindro(0.46, 0.04, (0, 0, 0.66), 'telhado_vermelho', lados=8)
    L.cone(0.44, 0.3, (0, 0, 0.7), 'telhado_vermelho', lados=8)
    L.esfera(0.03, (0, 0, 1.0), 'dourado')
    # Banquinhos
    for x in (-0.15, 0.15):
        L.cilindro(0.012, 0.2, (x, -0.55, 0), 'metal_escuro', lados=5)
        L.cilindro(0.05, 0.02, (x, -0.55, 0.2), 'vermelho', lados=8)


L.principal(__file__, construir)
