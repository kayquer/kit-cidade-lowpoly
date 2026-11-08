"""Mata (tile 2×2): grama com quatro árvores de alturas, formas e verdes diferentes (copa redonda e pinheiro),
arbustos e um tronco caído."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402


def construir():
    R.base('grama')
    L.arvore((-0.5, 0.45, 0), 1.3, 'verde_escuro')
    L.arvore((0.45, 0.5, 0), 1.0, 'verde', tipo='pinheiro')
    L.arvore((0.5, -0.45, 0), 0.85, 'folha')
    L.arvore((-0.45, -0.5, 0), 1.1, 'verde', tipo='pinheiro')
    L.arbusto((0.0, 0.05, 0), 0.14, 'verde_escuro')
    L.arbusto((-0.8, -0.05, 0), 0.1, 'folha')
    L.cano((0.1, -0.75, 0.04), (0.55, -0.85, 0.04), 0.04, 'madeira_escura', lados=6)


L.principal(__file__, construir)
