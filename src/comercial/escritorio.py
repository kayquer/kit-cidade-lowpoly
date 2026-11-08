"""Prédio de escritórios (1×1): bloco médio de seis andares com fachada de vidro azul em faixas e lajes
brancas aparentes, núcleo de concreto na lateral, entrada com pé-direito duplo, terraço com árvores e
bicicletário na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, andar, n = 0.15, 1.3, 1.2, 0.34, 6
    frente, direita = cy - prof / 2, larg / 2
    # Térreo recuado envidraçado
    L.caixa((larg - 0.1, prof - 0.1, 0.5), (0, cy, piso), 'vidro_escuro', chanfro=0.01)
    for x in (-0.6, -0.2, 0.2, 0.6):
        L.caixa((0.06, 0.06, 0.5), (x, frente + 0.03, piso), 'parede')
    z0 = piso + 0.5
    L.caixa((larg, prof, n * andar), (0, cy, z0), 'vidro', chanfro=0.01)
    for i in range(n + 1):                                                          # lajes aparentes
        L.caixa((larg + 0.04, prof + 0.04, 0.04), (0, cy, z0 + i * andar - 0.02), 'parede')
    for i in range(n):
        L.janelas('frente', frente, z0 + i * andar + 0.17, -0.55, 0.55, 4, 0.22, 0.2, cor='vidro_escuro')
    # Núcleo de concreto na lateral esquerda
    L.caixa((0.3, 0.5, n * andar + 0.65), (-larg / 2 - 0.1, cy + 0.2, piso), 'concreto', chanfro=0.015)
    # Lateral direita com brises verticais
    for i in range(5):
        L.caixa((0.04, 0.03, n * andar), (direita + 0.03, cy - 0.45 + i * 0.22, z0), 'parede')
    topo = z0 + n * andar
    # Terraço com árvores e casa de máquinas
    L.caixa((0.4, 0.4, 0.16), (0.3, cy + 0.3, topo + 0.02), 'concreto')
    L.caixa((0.5, 0.35, 0.06), (-0.25, cy - 0.2, topo + 0.02), 'terra')
    L.arvore((-0.35, cy - 0.2, topo + 0.08), 0.45, 'verde')
    L.arbusto((-0.12, cy - 0.2, topo + 0.08), 0.09, 'folha')
    # Marquise e bicicletário
    L.caixa((0.8, 0.3, 0.03), (0.1, frente - 0.15, piso + 0.48), 'metal_escuro')
    for x in (0.5, 0.65, 0.8):
        L.cano((x, -0.8, piso), (x, -0.8, piso + 0.12), 0.012, 'amarelo', lados=4)
    L.arvore((-0.75, -0.7, piso), 0.6, 'verde')


L.principal(__file__, construir)
