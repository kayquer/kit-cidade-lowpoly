"""Peças comuns dos veículos (src/veiculos/*.py): rodas, faróis, cabine de carro e cabine de caminhão.

Convenção: frente para -Y, comprimento ao longo de Y, x = 0 no centro, chão em z = 0.
Fica fora das pastas de categoria para gerar_todos.py e vitrine.py não o tratarem como modelo.
"""
import lib as L


def roda(xc, y, r=0.085, larg=0.06):
    """Roda escura com cubo cinza, eixo em X, centrada em (xc, y) com o centro a `r` do chão."""
    L.cilindro(r, larg, (xc - larg / 2, y, r), 'escuro', lados=10, rot=(0, 90, 0))
    sinal = 1 if xc > 0 else -1
    L.cilindro(r * 0.5, 0.01, (xc + sinal * larg / 2 - (0.01 if sinal < 0 else 0), y, r), 'metal', lados=6,
               rot=(0, 90, 0))


def rodas(larg, eixos, r=0.085):
    """Par de rodas em cada eixo (lista de y); ficam 0.02 para fora da carroceria de largura `larg`."""
    for y in eixos:
        for s in (-1, 1):
            roda(s * (larg / 2 - 0.01), y, r)


def farois(larg, y_frente, z, cor='flor_amarela', tam=0.06):
    for s in (-1, 1):
        L.caixa((tam, 0.012, 0.035), (s * (larg / 2 - tam / 2 - 0.025), y_frente - 0.006, z), cor)


def lanternas(larg, y_tras, z, tam=0.05):
    for s in (-1, 1):
        L.caixa((tam, 0.012, 0.035), (s * (larg / 2 - tam / 2 - 0.025), y_tras + 0.006, z), 'vermelho')


def carro(cor, comp=0.9, larg=0.42, teto=None, hatch=True):
    """Carro de passeio: carroceria, cabine de vidro com teto e colunas na cor, para-choques, faróis e rodas."""
    teto = teto or cor
    y0, y1 = -comp / 2, comp / 2
    L.caixa((larg, comp, 0.15), (0, 0, 0.07), cor, chanfro=0.03)
    # Cabine: perfil lateral (y, z) extrudado em X; para-brisa inclinado na frente
    tras = 0.36 if hatch else 0.24
    perfil = [(-0.2, 0), (tras, 0), (tras - (0.03 if hatch else 0.09), 0.14), (-0.08, 0.14)]
    L.prisma(perfil, larg - 0.05, (0, 0, 0.22), 'vidro', eixo='X')
    L.prisma([(-0.07, 0), (tras - (0.04 if hatch else 0.1), 0), (tras - (0.04 if hatch else 0.1), 0.025),
              (-0.07, 0.025)], larg - 0.04, (0, 0, 0.355), teto, eixo='X')
    L.caixa((larg - 0.035, 0.035, 0.14), (0, 0.08, 0.22), cor)          # coluna do meio
    # Para-choques, faróis, lanternas e rodas
    L.caixa((larg + 0.01, 0.04, 0.05), (0, y0 + 0.01, 0.06), 'escuro', chanfro=0.01)
    L.caixa((larg + 0.01, 0.04, 0.05), (0, y1 - 0.01, 0.06), 'escuro', chanfro=0.01)
    farois(larg, y0, 0.14)
    lanternas(larg, y1, 0.14)
    rodas(larg, (y0 + 0.2, y1 - 0.2))


def cabine_caminhao(cor, larg=0.5, y_frente=-0.7, comp=0.38, alt=0.46, z=0.1):
    """Cabine de caminhão (frente reta): bloco com para-brisa, janelas laterais, para-choque e faróis."""
    yc = y_frente + comp / 2
    L.caixa((larg, comp, alt), (0, yc, z), cor, chanfro=0.025)
    L.caixa((larg - 0.08, 0.012, alt * 0.38), (0, y_frente - 0.004, z + alt * 0.52), 'vidro')
    for s in (-1, 1):
        L.caixa((0.012, comp * 0.45, alt * 0.32), (s * (larg / 2 + 0.004), yc - comp * 0.15, z + alt * 0.55), 'vidro')
    L.caixa((larg + 0.02, 0.05, 0.07), (0, y_frente, z - 0.04), 'escuro', chanfro=0.01)
    farois(larg, y_frente, z + 0.07)
    L.caixa((larg * 0.5, 0.012, 0.06), (0, y_frente - 0.006, z + 0.05), 'metal_escuro')   # grade


def chassi(larg, y0, y1, z=0.06):
    L.caixa((larg - 0.1, y1 - y0, 0.06), (0, (y0 + y1) / 2, z), 'escuro')
