"""Porto (2×2, sobre a água): cais de concreto avançando sobre a água com defensas pretas e cabeços de
amarração, guindaste de pórtico laranja, pilhas de contêineres coloridos, armazém e um barco de carga atracado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def conteiner(x, y, z, cor, rot=0):
    L.caixa((0.22, 0.5, 0.2), (x, y, z), cor, rot=(0, 0, rot))
    return z + 0.2


def construir():
    # Água na frente (onde o barco atraca) e cais de concreto atrás
    L.caixa((4.0, 4.0, 0.1), (0, 0, 0), 'agua_funda')
    H = 0.32
    L.caixa((4.0, 2.4, H), (0, 0.8, 0), 'concreto', chanfro=0.02)
    L.caixa((4.0, 0.08, 0.03), (0, -0.36, H), 'amarelo')                          # borda do cais
    for x in (-1.6, -0.8, 0.0, 0.8, 1.6):
        L.caixa((0.18, 0.06, 0.16), (x, -0.42, 0.1), 'escuro', chanfro=0.02)       # defensas
        L.cilindro(0.04, 0.06, (x + 0.35, -0.25, H), 'metal_escuro', lados=6)      # cabeços
    for i in range(3):
        L.caixa((3.8, 0.05, 0.005), (0, 0.2 + i * 0.5, H), 'parede')                # trilhos/faixas

    # Guindaste de pórtico (pernas no cais, lança sobre a água)
    gx = -0.55
    for x in (gx - 0.4, gx + 0.4):
        for y in (-0.15, 0.6):
            L.caixa((0.08, 0.08, 1.5), (x, y, H), 'laranja')
    for y in (-0.15, 0.6):
        L.caixa((0.9, 0.08, 0.1), (gx, y, H + 1.4), 'laranja')
    L.caixa((0.14, 2.0, 0.12), (gx - 0.25, 0.0, H + 1.5), 'laranja', chanfro=0.01)
    L.caixa((0.14, 2.0, 0.12), (gx + 0.25, 0.0, H + 1.5), 'laranja', chanfro=0.01)
    L.caixa((0.3, 0.3, 0.2), (gx, -0.3, H + 1.62), 'amarelo', chanfro=0.01)          # carrinho/cabine
    L.cano((gx, -0.3, H + 1.62), (gx, -0.3, H + 0.95), 0.01, 'escuro', lados=4)
    conteiner(gx, -0.3, H + 0.75, 'telhado_azul', rot=90)                           # contêiner içado

    # Pilhas de contêineres no pátio
    pilhas = [(0.5, 0.6, ('vermelho', 'telhado_azul', 'verde')), (0.78, 0.6, ('amarelo', 'laranja')),
              (1.06, 0.6, ('verde_garrafa', 'vermelho', 'metal')), (1.34, 0.6, ('telhado_azul',)),
              (0.5, 1.2, ('laranja', 'metal')), (0.78, 1.2, ('verde',))]
    for (x, y, cores) in pilhas:
        z = H
        for cor in cores:
            z = conteiner(x, y, z, cor)
    # Armazém do porto (fundo esquerdo)
    L.caixa((1.3, 0.7, 0.55), (-1.25, 1.5, H), 'parede', chanfro=0.02)
    L.telhado(1.3, 0.7, 0.18, (-1.25, 1.5, H + 0.55), 'telhado_azul', beiral=0.05)
    L.placa(0.4, 0.38, (-1.25, 1.15, H + 0.38), 'metal_escuro', 'frente')
    L.janelas('direita', -0.6, H + 0.4, 1.3, 1.7, 2, 0.14, 0.1)

    # Barco de carga atracado na frente
    bx, by = 0.5, -1.15
    L.prisma([(-1.25, 0.05), (1.25, 0.05), (1.4, 0.3), (-1.45, 0.3)], 0.62, (bx, by, 0), 'vermelho', eixo='Y')
    L.prisma([(-1.25, 0.25), (1.25, 0.25), (1.4, 0.38), (-1.45, 0.38)], 0.63, (bx, by, 0), 'escuro', eixo='Y')
    L.caixa((0.4, 0.5, 0.42), (bx - 1.0, by, 0.38), 'parede', chanfro=0.01)          # ponte de comando
    L.caixa((0.42, 0.52, 0.08), (bx - 1.0, by, 0.62), 'vidro_escuro')
    L.cilindro(0.06, 0.18, (bx - 1.05, by, 0.8), 'amarelo', lados=6)                  # chaminé
    for i, cor in enumerate(('verde', 'amarelo', 'telhado_azul')):
        conteiner(bx - 0.4 + i * 0.4, by, 0.38, cor, rot=90)


L.principal(__file__, construir)
