"""Rua de asfalto reta (tile 2×2): liga as bordas -Y e +Y; asfalto de 1,3 com faixa central amarela tracejada,
calçadas de 0,35 dos dois lados com meio-fio, sobre o bloco de terreno."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base()
    R.rua_y()


L.principal(__file__, construir)
