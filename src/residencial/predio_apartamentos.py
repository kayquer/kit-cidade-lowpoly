"""Prédio de apartamentos (1×1): quatro andares creme com faixas terracota, sacadas com guarda-corpo de vidro
na frente, entrada com marquise, caixa d'água no telhado, bicicletas e canteiros na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, andar = 0.15, 1.4, 1.25, 0.45
    L.caixa((larg, prof, 0.4), (0, cy, piso), 'concreto', chanfro=0.02)               # térreo
    for i in range(4):
        z = piso + 0.4 + i * andar
        L.caixa((larg, prof, andar), (0, cy, z), 'creme', chanfro=0.015)
        L.caixa((larg + 0.03, prof + 0.03, 0.04), (0, cy, z), 'telhado_vermelho')     # faixa
        frente = cy - prof / 2
        L.janelas('frente', frente, z + 0.24, -0.6, -0.1, 2, 0.16, 0.2, moldura='parede')
        L.placa(0.36, 0.28, (0.32, frente, z + 0.22), 'vidro_escuro', 'frente')       # porta da sacada
        L.caixa((0.48, 0.2, 0.03), (0.32, frente - 0.1, z + 0.04), 'parede')          # laje da sacada
        L.caixa((0.48, 0.015, 0.12), (0.32, frente - 0.195, z + 0.07), 'vidro')
        L.janelas('direita', larg / 2, z + 0.24, cy - 0.4, cy + 0.4, 3, 0.16, 0.2, moldura='parede')
    topo = piso + 0.4 + 4 * andar
    L.caixa((larg + 0.06, prof + 0.06, 0.06), (0, cy, topo), 'concreto_escuro')
    # Caixa d'água e casa de máquinas
    L.caixa((0.5, 0.45, 0.3), (-0.3, cy + 0.2, topo + 0.06), 'parede', chanfro=0.015)
    L.caixa((0.42, 0.36, 0.2), (-0.3, cy + 0.2, topo + 0.36), 'telhado_azul', chanfro=0.015)
    L.caixa((0.26, 0.26, 0.18), (0.35, cy + 0.25, topo + 0.06), 'concreto')
    # Entrada com marquise
    frente = cy - prof / 2
    L.placa(0.34, 0.3, (-0.2, frente, piso + 0.16), 'vidro_escuro', 'frente')
    L.caixa((0.6, 0.35, 0.04), (-0.2, frente - 0.16, piso + 0.34), 'metal_escuro')
    L.janelas('frente', frente, piso + 0.22, 0.2, 0.6, 2, 0.14, 0.18, moldura='parede')
    # Calçada: canteiros e bicicletário
    for x in (-0.75, 0.75):
        L.caixa((0.3, 0.3, 0.08), (x, -0.75, piso), 'madeira')
        L.arbusto((x, -0.75, piso + 0.08), 0.12, 'verde')
    for x in (0.25, 0.4):
        L.cano((x, -0.78, piso), (x, -0.78, piso + 0.12), 0.012, 'amarelo', lados=4)


L.principal(__file__, construir)
