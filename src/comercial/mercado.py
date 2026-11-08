"""Mercado de bairro (1×1): galpão térreo branco com faixa vermelha, fachada de vidro, letreiro liso no alto,
cobertura na entrada, carrinhos de compra em fila e estacionamento pequeno com vagas pintadas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def carrinho(x, y):
    L.caixa((0.08, 0.12, 0.06), (x, y, 0.13), 'metal')
    L.cano((x, y + 0.06, 0.19), (x, y + 0.09, 0.22), 0.006, 'vermelho', lados=4)
    for dx in (-0.03, 0.03):
        L.cano((x + dx, y, 0.09), (x + dx, y, 0.13), 0.005, 'metal_escuro', lados=4)


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'asfalto', chanfro=0.02)
    piso = 0.08
    # Prédio ao fundo (frente para o estacionamento)
    cy, larg, prof, alt = 0.4, 1.7, 1.0, 0.62
    frente = cy - prof / 2
    L.caixa((1.75, 0.25, 0.015), (0, frente - 0.12, piso), 'concreto')                 # calçada da loja
    L.caixa((larg, prof, alt), (0, cy, piso), 'parede', chanfro=0.02)
    L.caixa((larg + 0.03, prof + 0.03, 0.12), (0, cy, piso + alt - 0.12), 'vermelho')
    L.caixa((larg, prof, 0.03), (0, cy, piso + alt), 'concreto_escuro')
    L.placa(0.9, 0.22, (0, frente - 0.02, piso + alt + 0.12), 'amarelo', 'frente')     # letreiro liso
    L.caixa((0.04, 0.04, 0.14), (-0.35, frente + 0.02, piso + alt), 'metal_escuro')
    L.caixa((0.04, 0.04, 0.14), (0.35, frente + 0.02, piso + alt), 'metal_escuro')
    L.placa(1.3, 0.34, (0, frente, piso + 0.2), 'vidro', 'frente')
    L.placa(0.3, 0.34, (0, frente - 0.005, piso + 0.2), 'vidro_escuro', 'frente')      # porta automática
    L.caixa((0.7, 0.3, 0.03), (0, frente - 0.15, piso + 0.4), 'vermelho')              # cobertura da entrada
    L.janelas('direita', larg / 2, piso + 0.3, cy - 0.3, cy + 0.3, 2, 0.25, 0.18)
    # Ar-condicionado no telhado
    L.caixa((0.25, 0.2, 0.12), (-0.5, cy + 0.2, piso + alt + 0.03), 'metal', chanfro=0.01)
    # Carrinhos
    for i in range(3):
        carrinho(0.55 + i * 0.1, frente - 0.12)
    # Estacionamento: vagas e canteiro
    for i in range(5):
        L.caixa((0.025, 0.45, 0.005), (-0.8 + i * 0.4, -0.55, piso), 'parede')
    L.caixa((1.75, 0.025, 0.005), (0, -0.8, piso), 'parede')
    L.caixa((0.35, 0.18, 0.06), (0.75, -0.85, piso), 'concreto')
    L.arbusto((0.75, -0.85, piso + 0.06), 0.08, 'verde')


L.principal(__file__, construir)
