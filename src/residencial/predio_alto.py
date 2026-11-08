"""Prédio alto residencial (1×1): torre de oito andares branca e azul com pilar de vidro, varandas alternadas,
térreo envidraçado com marquise, caixa d'água e painéis solares no topo e jardim na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'piso', chanfro=0.02)
    piso = 0.08
    cy, larg, prof, andar, n = 0.2, 1.2, 1.15, 0.36, 8
    frente = cy - prof / 2
    L.caixa((larg, prof, 0.42), (0, cy, piso), 'escuro', chanfro=0.015)               # térreo
    L.placa(1.0, 0.32, (0, frente, piso + 0.2), 'vidro_escuro', 'frente')
    L.caixa((1.3, 0.45, 0.04), (0, frente - 0.2, piso + 0.42), 'parede')               # marquise
    z0 = piso + 0.42
    L.caixa((larg, prof, n * andar), (0, cy, z0), 'parede', chanfro=0.02)
    L.caixa((0.3, 0.06, n * andar), (-0.42, frente - 0.01, z0), 'vidro')               # pilar de vidro (escada)
    for i in range(n):
        z = z0 + i * andar
        L.janelas('frente', frente, z + 0.19, -0.15, 0.55, 2, 0.24, 0.2)
        L.janelas('direita', larg / 2, z + 0.19, cy - 0.4, cy + 0.4, 3, 0.18, 0.2)
        if i % 2 == 0:                                                                # varandas alternadas
            L.caixa((0.6, 0.18, 0.03), (0.2, frente - 0.09, z + 0.02), 'telhado_azul')
            L.caixa((0.6, 0.015, 0.1), (0.2, frente - 0.175, z + 0.05), 'vidro')
    topo = z0 + n * andar
    L.caixa((larg + 0.05, prof + 0.05, 0.05), (0, cy, topo), 'telhado_azul')
    L.caixa((0.36, 0.36, 0.3), (-0.3, cy + 0.25, topo + 0.05), 'concreto', chanfro=0.01)
    L.cilindro(0.15, 0.2, (-0.3, cy + 0.25, topo + 0.35), 'cano', lados=8)              # caixa d'água
    for x in (0.08, 0.38):
        L.caixa((0.25, 0.42, 0.03), (x, cy - 0.05, topo + 0.12), 'metal', rot=(-25, 0, 0))
        L.caixa((0.22, 0.38, 0.01), (x, cy - 0.055, topo + 0.145), 'painel_solar', rot=(-25, 0, 0))
        L.caixa((0.03, 0.03, 0.12), (x, cy + 0.1, topo + 0.05), 'metal_escuro')
    # Jardim na calçada
    L.caixa((1.6, 0.25, 0.08), (0, -0.78, piso), 'madeira')
    for x, cor in ((-0.6, 'verde'), (-0.2, 'folha'), (0.55, 'verde_escuro')):
        L.arbusto((x, -0.78, piso + 0.08), 0.11, cor)
    L.arvore((0.75, -0.55, piso), 0.65, 'verde')


L.principal(__file__, construir)
