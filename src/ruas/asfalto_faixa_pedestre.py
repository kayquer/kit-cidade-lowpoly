"""Rua de asfalto reta com faixa de pedestres (tile 2×2): liga -Y e +Y, faixa zebrada branca no meio e a
faixa amarela central interrompida na travessia; rampas de acessibilidade nas calçadas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    R.rua_y(faixa=False)
    R.tracos_y(-1, -0.25, 2)
    R.tracos_y(0.25, 1, 2)
    R.zebra_y(0, larg=0.36)
    for s in (-1, 1):   # rampinha amarela (piso tátil) na calçada, nas duas pontas da faixa
        L.caixa((0.12, 0.3, 0.006), (s * 0.75, 0, R.Z_CALCADA), 'amarelo')


L.principal(__file__, construir)
