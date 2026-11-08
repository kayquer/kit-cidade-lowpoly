"""Agência bancária (1×1): prédio de pedra clara com escadaria, quatro colunas na fachada, frontão liso,
porta de vidro, caixa eletrônico em quiosque na lateral e cúpula baixa no telhado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, alt = 0.3, 1.4, 1.1, 0.8
    frente, direita = cy - prof / 2, larg / 2
    L.caixa((larg, prof, alt), (0, cy, piso), 'creme', chanfro=0.02)
    L.caixa((larg + 0.06, prof + 0.06, 0.1), (0, cy, piso + alt), 'parede')             # cornija
    L.caixa((larg - 0.1, prof - 0.1, 0.08), (0, cy, piso + alt + 0.1), 'pedra')
    L.cupula(0.3, (0, cy + 0.1, piso + alt + 0.18), 'agua_funda', lados=8, aneis=3)
    # Escadaria e pórtico
    for i, (lw, ly) in enumerate(((1.2, 0.5), (1.1, 0.4), (1.0, 0.3))):
        L.caixa((lw, ly, 0.05), (0, frente - ly / 2 + 0.02, piso + i * 0.05), 'parede')
    zc = piso + 0.15
    for x in (-0.36, -0.12, 0.12, 0.36):
        L.cilindro(0.055, 0.55, (x, frente - 0.18, zc), 'parede', lados=8)
        L.caixa((0.13, 0.13, 0.03), (x, frente - 0.18, zc), 'pedra')
    L.caixa((0.95, 0.3, 0.08), (0, frente - 0.13, zc + 0.55), 'parede')
    L.prisma([(-0.5, 0), (0.5, 0), (0, 0.2)], 0.3, (0, frente - 0.13, zc + 0.63), 'pedra', eixo='Y')
    L.placa(0.3, 0.42, (0, frente, zc + 0.21), 'vidro_escuro', 'frente')
    L.janelas('frente', frente, piso + 0.45, -0.62, -0.47, 1, 0.12, 0.38, moldura='parede')
    L.janelas('frente', frente, piso + 0.45, 0.47, 0.62, 1, 0.12, 0.38, moldura='parede')
    L.janelas('direita', direita, piso + 0.45, cy - 0.35, cy + 0.35, 3, 0.14, 0.38, moldura='parede')
    # Quiosque do caixa eletrônico na lateral direita (fora do prédio)
    kx, ky = 0.82, -0.45
    L.caixa((0.22, 0.3, 0.42), (kx, ky, piso), 'telhado_verde', chanfro=0.01)
    L.caixa((0.26, 0.34, 0.03), (kx, ky, piso + 0.42), 'parede')
    L.placa(0.16, 0.12, (kx, ky - 0.15, piso + 0.28), 'vidro_escuro', 'frente')         # tela
    L.placa(0.12, 0.04, (kx, ky - 0.155, piso + 0.18), 'metal', 'frente')
    # Canteiros e poste
    for x in (-0.75, 0.75):
        L.arbusto((x, -0.85, piso), 0.1, 'verde_escuro')
    L.arvore((-0.8, -0.35, piso), 0.6, 'verde')


L.principal(__file__, construir)
