"""Terreno de grama (tile 2×2): bloco de terra de z -0,3 a 0 com a lâmina de grama no topo; base de todas as
outras peças de terreno e de rua."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base('grama')


L.principal(__file__, construir)
