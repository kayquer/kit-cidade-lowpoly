"""Hotel (1×1): torre de sete andares creme e terracota com janelas em fita, marquise grande sobre a entrada
de carros, porta giratória de vidro, bandeiras na fachada e piscina com espreguiçadeiras e guarda-sol na
cobertura."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, andar, n = 0.3, 1.4, 1.1, 0.34, 7
    frente, direita = cy - prof / 2, larg / 2
    L.caixa((larg + 0.1, prof + 0.1, 0.5), (0, cy, piso), 'telhado_vermelho', chanfro=0.015)  # embasamento
    L.placa(0.5, 0.38, (0, frente - 0.05, piso + 0.22), 'vidro_escuro', 'frente')
    L.cilindro(0.12, 0.38, (0, frente - 0.12, piso), 'vidro', lados=8)                        # porta giratória
    z0 = piso + 0.5
    L.caixa((larg, prof, n * andar), (0, cy, z0), 'creme', chanfro=0.02)
    for i in range(n):
        z = z0 + i * andar
        L.caixa((larg + 0.02, 0.06, 0.12), (0, frente - 0.01, z + 0.12), 'vidro_escuro')     # janela em fita
        L.caixa((0.06, prof * 0.8, 0.12), (direita + 0.01, cy, z + 0.12), 'vidro_escuro')
    L.caixa((larg + 0.05, prof + 0.05, 0.05), (0, cy, z0 + n * andar), 'telhado_vermelho')
    # Faixa vertical com o "logo" liso
    L.caixa((0.22, 0.04, n * andar - 0.2), (-0.5, frente - 0.03, z0 + 0.1), 'telhado_vermelho')
    L.placa(0.14, 0.14, (-0.5, frente - 0.05, z0 + n * andar - 0.3), 'dourado', 'frente')
    # Marquise sobre a entrada de carros, com dois pilares
    L.caixa((1.3, 0.75, 0.05), (0, frente - 0.4, piso + 0.5), 'parede', chanfro=0.01)
    for x in (-0.55, 0.55):
        L.cilindro(0.035, 0.5, (x, frente - 0.7, piso), 'metal', lados=6)
    L.caixa((1.2, 0.5, 0.01), (0, -0.62, piso), 'telhado_vermelho')                           # tapete vermelho
    # Bandeiras
    for x, cor in ((0.45, 'telhado_azul'), (0.6, 'verde'), (0.75, 'amarelo')):
        L.cano((x, -0.88, piso), (x, -0.88, piso + 0.85), 0.01, 'metal', lados=4)
        L.caixa((0.01, 0.12, 0.08), (x, -0.82, piso + 0.75), cor)
    # Cobertura: piscina, deque, espreguiçadeiras e guarda-sol
    topo = z0 + n * andar + 0.05
    L.caixa((1.3, 1.0, 0.03), (0, cy, topo), 'madeira')
    L.tanque(0.75, 0.5, 0.08, (-0.15, cy + 0.15, topo + 0.03), cor_agua='agua', cor='parede', parede=0.04, nivel=0.02)
    for x in (0.38, 0.55):
        L.caixa((0.12, 0.26, 0.03), (x, cy - 0.25, topo + 0.03), 'parede', rot=(8, 0, 0))
    L.cano((0.5, cy + 0.2, topo + 0.03), (0.5, cy + 0.2, topo + 0.3), 0.008, 'metal', lados=4)
    L.cone(0.16, 0.07, (0.5, cy + 0.2, topo + 0.27), 'laranja', lados=8)
    L.caixa((1.36, 0.02, 0.08), (0, cy - prof / 2 + 0.03, topo + 0.03), 'vidro')              # guarda-corpo


L.principal(__file__, construir)
