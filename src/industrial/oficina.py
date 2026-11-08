"""Oficina Mecânica (1×1): prédio baixo com dois boxes de portão aberto, um carro no elevador, pilha de
pneus, tambores de óleo, bancada de ferramentas, toldo listrado e placa genérica com uma chave inglesa."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def pneu(x, y, z):
    L.anel(0.11, 0.05, 0.07, (x, y, z), 'escuro', lados=8)
    return z + 0.07


def construir():
    L.caixa((2.0, 2.0, 0.06), (0, 0, 0), 'concreto', chanfro=0.02)
    piso = 0.06
    L.caixa((1.5, 0.6, 0.008), (-0.15, -0.65, piso), 'asfalto')

    bx, by, w, d, h = -0.15, 0.4, 1.5, 1.0, 0.72
    L.caixa((w, d, h), (bx, by, piso), 'creme', chanfro=0.025)
    L.caixa((w + 0.04, d + 0.04, 0.1), (bx, by, piso + h), 'telhado_azul')
    frente = by - d / 2
    # Dois boxes com portões abertos (interior escuro, portão recolhido em cima)
    for gx in (-0.5, 0.2):
        L.placa(0.56, 0.48, (gx, frente, piso + 0.48), 'escuro', 'frente', espessura=0.02)
        L.placa(0.6, 0.08, (gx, frente - 0.01, piso + 0.58), 'metal', 'frente', espessura=0.03)
    # Carro no elevador (box da esquerda, metade para fora)
    cx, cy, cz = -0.5, frente - 0.05, piso + 0.12
    L.caixa((0.04, 0.5, 0.12), (cx - 0.16, cy, piso), 'amarelo')
    L.caixa((0.04, 0.5, 0.12), (cx + 0.16, cy, piso), 'amarelo')
    L.caixa((0.34, 0.6, 0.12), (cx, cy, cz), 'vermelho', chanfro=0.02)
    L.caixa((0.3, 0.32, 0.1), (cx, cy + 0.04, cz + 0.12), 'vidro_escuro', chanfro=0.015)
    for wy in (-0.2, 0.2):
        for wx in (-0.17, 0.17):
            L.cilindro(0.06, 0.04, (cx + wx + (0.02 if wx > 0 else -0.02), cy + wy, cz + 0.02), 'escuro', lados=8,
                       rot=(0, 90, 0))
    # Toldo listrado sobre os boxes
    for i in range(6):
        cor = 'parede' if i % 2 else 'laranja'
        L.caixa((0.25, 0.3, 0.025), (bx - 0.625 + i * 0.25, frente - 0.12, piso + 0.66), cor, rot=(-15, 0, 0))
    # Placa genérica com chave inglesa no telhado
    L.caixa((0.5, 0.05, 0.25), (bx + 0.3, by, piso + h + 0.1), 'parede', chanfro=0.01)
    L.caixa((0.28, 0.02, 0.04), (bx + 0.3, by - 0.03, piso + h + 0.21), 'metal_escuro', rot=(0, 25, 0))
    L.cilindro(0.045, 0.02, (bx + 0.42, by - 0.03, piso + h + 0.27), 'metal_escuro', lados=6, rot=(90, 0, 0))
    L.janelas('direita', bx + w / 2, piso + 0.4, by - 0.25, by + 0.25, 2, 0.2, 0.18)

    # Pilha de pneus, tambores e bancada no pátio direito
    z = piso
    for _ in range(4):
        z = pneu(0.78, -0.25, z)
    z = pneu(0.78, -0.55, piso)
    pneu(0.78, -0.55, z)
    pneu(0.55, -0.82, piso)
    for (tx, ty, cor) in ((0.8, 0.5, 'telhado_azul'), (0.8, 0.25, 'vermelho')):
        L.cilindro(0.08, 0.22, (tx, ty, piso), cor, lados=8)
        L.cilindro(0.082, 0.02, (tx, ty, piso + 0.15), 'escuro', lados=8)
    L.caixa((0.14, 0.4, 0.04), (0.8, 0.0, piso + 0.2), 'madeira')                        # bancada
    for py in (-0.17, 0.17):
        L.caixa((0.03, 0.03, 0.2), (0.8, py, piso), 'metal_escuro')
    L.caixa((0.1, 0.12, 0.06), (0.8, 0.05, piso + 0.24), 'vermelho')                     # caixa de ferramentas


L.principal(__file__, construir)
