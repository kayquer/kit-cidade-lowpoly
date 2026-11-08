"""
Peças comuns das ruas e do terreno modulares (tiles 2 × 2). Domínio público (CC0 1.0).

Perfil padrão (Blender, antes do giro de 180° da exportação):
- Tile: x e y de -1 a +1. Bloco de terreno de z -0.3 a 0 (terra) com uma lâmina de grama no topo (z -0.03 a 0).
- Asfalto: faixa de 1.3 centrada (|x| ≤ 0.65 numa rua ao longo de Y), z 0 a 0.04.
- Calçada: 0.35 de cada lado (0.65 ≤ |x| ≤ 1), z 0 a 0.07, com meio-fio de 0.04 na borda do asfalto.
- Água: superfície em z -0.12, leito de z -0.3 a -0.2. Margem de areia em z -0.06, 0.18 de largura.
"""
import math

import lib as L

MEIO = 0.65          # meia largura do asfalto
CALCADA = 0.35       # largura da calçada (MEIO + CALCADA = 1)
Z_ASFALTO = 0.04
Z_CALCADA = 0.07
MEIO_FIO = 0.04
Z_AGUA = -0.12
Z_LEITO = -0.2
Z_AREIA = -0.06
AREIA = 0.18
BASE = -0.3
GRAMA = 0.03


def poligono(pts, z0, z1, cor):
    """Contorno 2D (x, y) extrudado de z0 até z1."""
    return L.prisma(list(pts), z1 - z0, (0, 0, z0), cor, eixo='Z')


def arco(cx, cy, r, a0, a1, n=10):
    """Pontos de um arco de círculo (ângulos em graus, de a0 até a1, inclusive)."""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def anel(cx, cy, r0, r1, a0, a1, z0, z1, cor, n=10):
    """Faixa em arco (coroa) entre os raios r0 < r1."""
    return poligono(arco(cx, cy, r1, a0, a1, n) + list(reversed(arco(cx, cy, r0, a0, a1, n))), z0, z1, cor)


def base(topo='grama'):
    """Bloco de terreno 2 × 2: terra de -0.3 a -0.03 e lâmina `topo` até z 0."""
    L.caixa((2, 2, -GRAMA - BASE), (0, 0, BASE), 'terra')
    L.caixa((2, 2, GRAMA), (0, 0, -GRAMA), topo)


def rua_y(y0=-1, y1=1, faixa=True, tracos=4):
    """Trecho reto ao longo de Y entre y0 e y1: asfalto, calçadas e meio-fios dos dois lados."""
    comp = y1 - y0
    cy = (y0 + y1) / 2
    L.caixa((2 * MEIO, comp, Z_ASFALTO), (0, cy, 0), 'asfalto')
    for s in (-1, 1):
        L.caixa((CALCADA - MEIO_FIO, comp, Z_CALCADA), (s * (MEIO + MEIO_FIO + (CALCADA - MEIO_FIO) / 2), cy, 0), 'piso')
        L.caixa((MEIO_FIO, comp, Z_CALCADA + 0.005), (s * (MEIO + MEIO_FIO / 2), cy, 0), 'concreto')
    if faixa:
        tracos_y(y0, y1, tracos)


def tracos_y(y0, y1, n=4, x=0.0, cor='amarelo'):
    """Faixa central tracejada ao longo de Y (n traços, meio vão nas pontas para casar entre tiles)."""
    passo = (y1 - y0) / n
    for i in range(n):
        L.caixa((0.04, passo * 0.5, 0.004), (x, y0 + passo * (i + 0.5), Z_ASFALTO), cor)


def zebra_y(yc, larg=0.24):
    """Faixa de pedestres atravessando uma rua ao longo de Y, centrada em y = yc."""
    n = 6
    passo = 2 * MEIO / n
    for i in range(n):
        L.caixa((passo * 0.55, larg, 0.004), (-MEIO + passo * (i + 0.5), yc, Z_ASFALTO), 'parede')


def zebra_x(xc, larg=0.24):
    """Faixa de pedestres atravessando uma rua ao longo de X, centrada em x = xc."""
    n = 6
    passo = 2 * MEIO / n
    for i in range(n):
        L.caixa((larg, passo * 0.55, 0.004), (xc, -MEIO + passo * (i + 0.5), Z_ASFALTO), 'parede')


def calcada_canto(x0, x1, y0, y1):
    """Retângulo de calçada (sem meio-fio)."""
    L.caixa((x1 - x0, y1 - y0, Z_CALCADA), ((x0 + x1) / 2, (y0 + y1) / 2, 0), 'piso')


def capim(x, y, h=0.1, z=0.0):
    L.cone(0.04, h, (x, y, z), 'verde', lados=4)
    L.cone(0.03, h * 0.8, (x + 0.03, y + 0.02, z), 'folha', lados=4)


def agua_fundo():
    """Leito (terra escura) de -0.3 a -0.2 no tile todo."""
    L.caixa((2, 2, Z_LEITO - BASE), (0, 0, BASE), 'terra')


def banco(x, y, rz=0):
    """Banquinho de praça simples (assento de madeira sobre dois pés)."""
    L.caixa((0.34, 0.1, 0.02), (x, y, 0.1), 'madeira', rot=(0, 0, rz))
    for d in (-0.13, 0.13):
        dx, dy = d * math.cos(math.radians(rz)), d * math.sin(math.radians(rz))
        L.caixa((0.025, 0.09, 0.1), (x + dx, y + dy, 0), 'escuro', rot=(0, 0, rz))
