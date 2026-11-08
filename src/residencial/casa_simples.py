"""Casa simples (1×1): casa térrea creme com telhado de duas águas de telha vermelha, varandinha coberta na
frente, porta de madeira, janelas com moldura, muro baixo com portão e um quintal com árvore."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.08
    L.caixa((0.3, 0.75, 0.015), (0.1, -0.55, piso), 'piso')            # caminho até a porta
    # Corpo da casa
    cx, cy, larg, prof, alt = 0.05, 0.2, 1.2, 0.95, 0.62
    L.caixa((larg, prof, alt), (cx, cy, piso), 'creme', chanfro=0.02)
    L.caixa((larg + 0.04, prof + 0.04, 0.05), (cx, cy, piso), 'concreto_escuro')   # rodapé
    L.telhado(larg, prof, 0.42, (cx, cy, piso + alt), 'telhado_vermelho', beiral=0.1)
    frente = cy - prof / 2
    L.placa(0.2, 0.38, (0.1, frente, piso + 0.21), 'madeira_escura', 'frente')
    L.janelas('frente', frente, piso + 0.36, -0.5, -0.15, 1, 0.22, 0.2, moldura='parede')
    L.janelas('frente', frente, piso + 0.36, 0.35, 0.6, 1, 0.2, 0.2, moldura='parede')
    L.janelas('direita', cx + larg / 2, piso + 0.36, cy - 0.3, cy + 0.3, 2, 0.2, 0.2, moldura='parede')
    # Varandinha: piso, dois pilares e telhadinho
    L.caixa((0.6, 0.3, 0.04), (0.1, frente - 0.15, piso), 'pedra')
    for x in (-0.17, 0.37):
        L.caixa((0.04, 0.04, 0.42), (x, frente - 0.27, piso + 0.04), 'madeira')
    L.caixa((0.7, 0.36, 0.03), (0.1, frente - 0.16, piso + 0.46), 'telhado_vermelho', rot=(-12, 0, 0))
    # Chaminé
    L.caixa((0.12, 0.12, 0.3), (-0.3, cy + 0.15, piso + alt + 0.15), 'parede', chanfro=0.01)
    # Muro baixo com portão aberto na frente
    m = 0.9
    L.caixa((0.62, 0.05, 0.12), (-0.58, -m, piso), 'parede', chanfro=0.008)
    L.caixa((0.52, 0.05, 0.12), (0.63, -m, piso), 'parede', chanfro=0.008)
    L.caixa((0.05, 1.8, 0.12), (-m, 0, piso), 'parede', chanfro=0.008)
    L.caixa((0.05, 1.8, 0.12), (m, 0, piso), 'parede', chanfro=0.008)
    L.caixa((0.3, 0.02, 0.1), (0.27, -m + 0.11, piso), 'metal_escuro', rot=(0, 0, 50))   # portão aberto para dentro
    # Quintal
    L.arvore((-0.6, -0.55, piso), 0.7, 'verde')
    L.arbusto((0.65, -0.65, piso), 0.12, 'verde_escuro')
    L.esfera(0.025, (0.62, -0.72, piso + 0.12), 'flor_rosa')


L.principal(__file__, construir)
