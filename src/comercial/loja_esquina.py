"""Loja de esquina (1×1): sobradinho comercial verde-água com vitrine grande, toldo listrado laranja e branco
na frente e na lateral, letreiro liso, moradia em cima, caixotes de frutas e vasos na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def toldo_frente(x0, x1, y, z, listras=7):
    w = (x1 - x0) / listras
    for i in range(listras):
        cor = 'laranja' if i % 2 == 0 else 'parede'
        L.caixa((w, 0.32, 0.02), (x0 + w * (i + 0.5), y - 0.14, z), cor, rot=(-20, 0, 0))


def toldo_lado(y0, y1, x, z, listras=5):
    w = (y1 - y0) / listras
    for i in range(listras):
        cor = 'laranja' if i % 2 == 0 else 'parede'
        L.caixa((0.32, w, 0.02), (x + 0.14, y0 + w * (i + 0.5), z), cor, rot=(0, -20, 0))


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cx, cy, larg, prof = -0.05, 0.15, 1.45, 1.25
    frente, direita = cy - prof / 2, cx + larg / 2
    L.caixa((larg, prof, 0.6), (cx, cy, piso), 'agua', chanfro=0.02)
    L.caixa((larg, prof, 0.5), (cx, cy, piso + 0.6), 'creme', chanfro=0.02)
    L.caixa((larg + 0.05, prof + 0.05, 0.06), (cx, cy, piso + 1.1), 'parede')
    L.caixa((larg + 0.02, prof + 0.02, 0.1), (cx, cy, piso + 0.56), 'parede')          # faixa do letreiro
    L.placa(0.7, 0.08, (cx - 0.1, frente - 0.01, piso + 0.66), 'telhado_verde', 'frente')
    # Vitrines e porta
    L.placa(0.75, 0.38, (cx - 0.25, frente, piso + 0.25), 'vidro', 'frente')
    L.placa(0.22, 0.42, (cx + 0.45, frente, piso + 0.23), 'vidro_escuro', 'frente')
    L.placa(0.65, 0.38, (direita, cy - 0.15, piso + 0.25), 'vidro', 'direita')
    # Mercadorias atrás da vitrine
    for i, cor in enumerate(('vermelho', 'amarelo', 'verde', 'laranja')):
        L.caixa((0.12, 0.08, 0.1), (cx - 0.52 + i * 0.18, frente + 0.06, piso + 0.06), cor)
    # Toldos
    toldo_frente(cx - larg / 2, cx + larg / 2, frente, piso + 0.48)
    toldo_lado(cy - prof / 2, cy + 0.3, direita, piso + 0.48)
    # Andar de cima
    L.janelas('frente', frente, piso + 0.85, cx - 0.5, cx + 0.5, 3, 0.2, 0.22, moldura='parede')
    L.janelas('direita', direita, piso + 0.85, cy - 0.35, cy + 0.35, 2, 0.2, 0.22, moldura='parede')
    # Calçada: caixotes de frutas e vasos
    for i, cor in enumerate(('vermelho', 'amarelo', 'verde')):
        x = cx - 0.55 + i * 0.22
        L.caixa((0.18, 0.14, 0.08), (x, frente - 0.2, piso), 'madeira')
        L.esfera(0.06, (x, frente - 0.2, piso + 0.08), cor, escala=(1.2, 0.9, 0.5))
    L.cilindro(0.08, 0.1, (0.82, -0.82, piso), 'telhado_vermelho', lados=6)
    L.arbusto((0.82, -0.82, piso + 0.1), 0.1, 'verde')


L.principal(__file__, construir)
