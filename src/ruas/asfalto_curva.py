"""Rua de asfalto em curva (tile 2×2): liga as bordas -Y e +X num arco de 90° centrado no canto (+1, -1);
faixa amarela tracejada no eixo, calçada interna e externa com meio-fio acompanhando a curva."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402

C = (1, -1)                      # centro da curva (canto do tile)
R_IN = 1 - R.MEIO                # 0.35: raio da borda interna do asfalto
R_OUT = 1 + R.MEIO               # 1.65: raio da borda externa do asfalto


def construir():
    R.base()
    cx, cy = C
    # Asfalto (coroa de 90° a 180°: de -Y para +X passando por dentro do tile)
    R.anel(cx, cy, R_IN, R_OUT, 90, 180, 0, R.Z_ASFALTO, 'asfalto', n=12)
    # Calçada interna (quarto de círculo no canto) + meio-fio
    R.poligono([C] + R.arco(cx, cy, R_IN - R.MEIO_FIO, 90, 180, 8), 0, R.Z_CALCADA, 'piso')
    R.anel(cx, cy, R_IN - R.MEIO_FIO, R_IN, 90, 180, 0, R.Z_CALCADA + 0.005, 'concreto', n=8)
    # Calçada externa: faixa em arco da mesma largura da reta (o canto de fora fica com a grama do bloco)
    R.anel(cx, cy, R_OUT + R.MEIO_FIO, 2, 90, 180, 0, R.Z_CALCADA, 'piso', n=12)
    R.anel(cx, cy, R_OUT, R_OUT + R.MEIO_FIO, 90, 180, 0, R.Z_CALCADA + 0.005, 'concreto', n=12)
    L.arbusto((-0.62, 0.62, 0), 0.12, 'verde_escuro')            # um arbusto no canto de grama
    L.arbusto((-0.82, 0.3, 0), 0.08, 'folha')
    # Faixa central tracejada no raio 1 (4 traços, meio vão nas pontas, como na reta)
    for i in range(4):
        a0 = 180 - 90 * (i + 0.25) / 4
        a1 = 180 - 90 * (i + 0.75) / 4
        R.anel(cx, cy, 0.98, 1.02, a1, a0, R.Z_ASFALTO, R.Z_ASFALTO + 0.004, 'amarelo', n=2)


L.principal(__file__, construir)
