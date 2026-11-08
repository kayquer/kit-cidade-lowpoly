"""Fim de rua com balão de retorno (tile 2×2): só liga a borda -Y; a rua abre num círculo de asfalto com um
canteiro redondo no meio (arbusto e flores), calçada com meio-fio contornando o balão."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402

CY = 0.05          # centro do balão
RAIO = 0.8         # raio do asfalto do balão


def construir():
    R.base()
    M, F, ZC = R.MEIO, R.MEIO_FIO, R.Z_CALCADA
    # Ângulo em que a rua (|x| = 0.65) encontra o círculo
    a = math.degrees(math.asin(M / RAIO))            # medido a partir de -Y
    a_dir, a_esq = -90 + a, 270 - a                  # pontos de junção (direita e esquerda)
    yj = CY - RAIO * math.cos(math.radians(a))
    # Asfalto: trecho reto + círculo (um contorno só)
    contorno = [(-M, -1), (M, -1)] + R.arco(0, CY, RAIO, a_dir, a_esq, 16)
    R.poligono(contorno, 0, R.Z_ASFALTO, 'asfalto')
    # Meio-fio: retas ao longo da rua e arco em volta do balão
    for s in (-1, 1):
        L.caixa((F, yj + 1, ZC + 0.005), (s * (M + F / 2), (yj - 1) / 2, 0), 'concreto')
    R.anel(0, CY, RAIO, RAIO + F, a_dir, a_esq, 0, ZC + 0.005, 'concreto', n=16)
    # Calçada: duas metades (esquerda e direita) do lado de fora do meio-fio
    meia = [a_dir + (90 - a_dir) * i / 8 for i in range(9)]                  # da junção direita até o topo
    arco_dir = [(math.cos(math.radians(t)) * (RAIO + F), CY + math.sin(math.radians(t)) * (RAIO + F)) for t in meia]
    direita = [(M + F, -1), (1, -1), (1, 1), (0, 1)] + list(reversed(arco_dir))
    R.poligono(direita, 0, ZC, 'piso')
    esquerda = [(-x, y) for (x, y) in reversed(direita)]
    R.poligono(esquerda, 0, ZC, 'piso')
    # Canteiro central
    L.cilindro(0.26, 0.08, (0, CY, 0), 'concreto', lados=10)
    L.cilindro(0.22, 0.085, (0, CY, 0), 'grama', lados=10)
    L.arbusto((0, CY, 0.085), 0.13, 'verde')
    for (x, y, cor) in ((0.12, CY - 0.08, 'flor_rosa'), (-0.1, CY + 0.1, 'flor_amarela'), (-0.12, CY - 0.06, 'flor_rosa')):
        L.esfera(0.025, (x, y, 0.13), cor)
    R.tracos_y(-1, -0.25, 2)


L.principal(__file__, construir)
