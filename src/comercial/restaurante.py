"""Restaurante (1×1): casa de esquina terracota com telhado de telha, janelões, chaminé do forno a lenha,
letreiro liso, deque de madeira na calçada com mesas, cadeiras e guarda-sóis coloridos e vasos."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def mesa(x, y, z, cor_sol):
    L.cilindro(0.08, 0.015, (x, y, z + 0.12), 'parede', lados=8)
    L.cano((x, y, z), (x, y, z + 0.12), 0.01, 'metal_escuro', lados=4)
    for dx in (-0.13, 0.13):
        L.caixa((0.07, 0.07, 0.07), (x + dx, y, z), 'madeira_escura')
    L.cano((x, y, z + 0.13), (x, y, z + 0.42), 0.008, 'metal', lados=4)
    L.cone(0.17, 0.08, (x, y, z + 0.38), cor_sol, lados=8)


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, alt = 0.4, 1.5, 0.95, 0.65
    frente, direita = cy - prof / 2, larg / 2
    L.caixa((larg, prof, alt), (0, cy, piso), 'telhado_vermelho', chanfro=0.02)
    L.caixa((larg + 0.03, prof + 0.03, 0.08), (0, cy, piso), 'madeira_escura')
    L.telhado(larg, prof, 0.35, (0, cy, piso + alt), 'marrom', beiral=0.08)
    L.placa(0.7, 0.12, (-0.2, frente - 0.01, piso + 0.56), 'creme', 'frente')            # letreiro liso
    L.placa(0.22, 0.38, (0.45, frente, piso + 0.2), 'madeira_escura', 'frente')
    L.janelas('frente', frente, piso + 0.25, -0.65, 0.2, 2, 0.32, 0.3, moldura='creme')
    L.janelas('direita', direita, piso + 0.3, cy - 0.25, cy + 0.25, 2, 0.22, 0.26, moldura='creme')
    # Chaminé do forno
    L.caixa((0.16, 0.16, 0.5), (-0.5, cy + 0.2, piso + alt + 0.05), 'pedra', chanfro=0.01)
    L.caixa((0.2, 0.2, 0.04), (-0.5, cy + 0.2, piso + alt + 0.55), 'concreto_escuro')
    # Deque com mesas
    L.caixa((1.7, 0.85, 0.04), (0, -0.45, piso), 'madeira', chanfro=0.008)
    for i in range(5):
        L.caixa((1.7, 0.01, 0.002), (0, -0.82 + i * 0.17, piso + 0.04), 'madeira_escura')
    mesa(-0.5, -0.3, piso + 0.04, 'vermelho')
    mesa(0.05, -0.55, piso + 0.04, 'amarelo')
    mesa(0.55, -0.3, piso + 0.04, 'verde')
    # Gradil e vasos nos cantos do deque
    for x in (-0.8, 0.8):
        L.cilindro(0.07, 0.1, (x, -0.8, piso + 0.04), 'telhado_vermelho', lados=6)
        L.arbusto((x, -0.8, piso + 0.14), 0.09, 'verde')


L.principal(__file__, construir)
