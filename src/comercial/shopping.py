"""Shopping (2×2): galeria baixa em L com fachada de vidro e lojas, claraboia em arco sobre o corredor
central, entrada com marquise, telhado verde em parte da cobertura, estacionamento com vagas, árvores e
ponto de táxi na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((3.9, 3.9, 0.08), (0, 0, 0), 'asfalto', chanfro=0.02)
    piso = 0.08
    # Blocos: corpo ao fundo e ala à direita (em L)
    L.caixa((3.4, 1.6, 0.85), (0, 0.95, piso), 'parede', chanfro=0.03)
    L.caixa((1.1, 1.4, 0.75), (1.15, -0.55, piso), 'creme', chanfro=0.03)
    L.caixa((3.45, 1.65, 0.05), (0, 0.95, piso + 0.85), 'concreto_escuro')
    L.caixa((1.15, 1.45, 0.05), (1.15, -0.55, piso + 0.75), 'concreto_escuro')
    frente = 0.95 - 0.8
    # Fachada de lojas com toldos coloridos
    cores = ('vermelho', 'telhado_azul', 'amarelo', 'verde', 'laranja')
    for i, cor in enumerate(cores):
        x = -1.5 + i * 0.4
        L.placa(0.32, 0.36, (x, frente, piso + 0.24), 'vidro', 'frente')
        L.caixa((0.34, 0.18, 0.02), (x, frente - 0.08, piso + 0.45), cor, rot=(-20, 0, 0))
    # Entrada principal com marquise e corredor com claraboia
    L.placa(0.6, 0.6, (0.35, frente, piso + 0.32), 'vidro_escuro', 'frente')
    L.caixa((1.0, 0.5, 0.05), (0.35, frente - 0.25, piso + 0.66), 'parede')
    for x in (-0.1, 0.8):
        L.cano((x, frente - 0.45, piso), (x, frente - 0.45, piso + 0.66), 0.025, 'metal', lados=6)
    for i in range(5):                                         # claraboia em "arco" facetado
        z = piso + 0.9
        L.caixa((0.8, 0.28, 0.02), (0.35, 0.95 - 0.56 + i * 0.28, z + (0.12 if i in (1, 2, 3) else 0.04)),
                'vidro', rot=(0, 0, 0))
    L.caixa((0.06, 1.4, 0.18), (-0.07, 0.95, piso + 0.88), 'metal')
    L.caixa((0.06, 1.4, 0.18), (0.77, 0.95, piso + 0.88), 'metal')
    # Telhado verde e máquinas
    L.caixa((1.3, 1.2, 0.04), (-1.0, 0.95, piso + 0.9), 'telhado_verde')
    L.arbusto((-1.3, 1.1, piso + 0.94), 0.12, 'verde')
    L.arbusto((-0.8, 0.8, piso + 0.94), 0.1, 'folha')
    L.caixa((0.4, 0.3, 0.15), (1.15, -0.4, piso + 0.8), 'metal', chanfro=0.01)
    # Ala direita: janelas na lateral e vitrine
    L.janelas('direita', 1.7, piso + 0.35, -1.1, 0.0, 3, 0.25, 0.3)
    L.placa(0.8, 0.32, (1.15, -1.25, piso + 0.24), 'vidro', 'frente')
    L.caixa((0.9, 0.2, 0.02), (1.15, -1.33, piso + 0.45), 'roxo', rot=(-20, 0, 0))
    # Estacionamento
    for i in range(6):
        L.caixa((0.025, 0.55, 0.005), (-1.75 + i * 0.4, -0.9, piso), 'parede')
    L.caixa((2.2, 0.025, 0.005), (-0.65, -1.2, piso), 'parede')
    L.caixa((2.4, 0.3, 0.05), (-0.6, -1.7, piso), 'grama')
    for x in (-1.6, -0.6, 0.4):
        L.arvore((x, -1.7, piso + 0.05), 0.7, 'verde')
    # Ponto de táxi
    L.caixa((0.4, 0.2, 0.015), (1.4, -1.6, piso), 'amarelo')


L.principal(__file__, construir)
