"""Capivara estilizada num pedaço de grama da margem: corpo marrom robusto, cabeça quadrada olhando para a
frente (-Y), focinho escuro, orelhinhas, olhos e pernas curtas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.32, 0.015, (0, 0, 0), 'grama', lados=10)
    for x in (-0.07, 0.07):                                             # pernas
        for y in (-0.1, 0.12):
            L.cilindro(0.025, 0.08, (x, y, 0.015), 'madeira_escura', lados=5)
    L.esfera(0.14, (0, 0.02, 0.17), 'madeira', escala=(0.85, 1.4, 0.8), sub=1)    # corpo
    L.caixa((0.14, 0.14, 0.12), (0, -0.2, 0.15), 'madeira', chanfro=0.03)       # cabeça
    L.caixa((0.12, 0.06, 0.08), (0, -0.28, 0.15), 'madeira_escura', chanfro=0.02)  # focinho
    L.caixa((0.05, 0.012, 0.02), (0, -0.312, 0.19), 'escuro')                     # nariz
    for x in (-0.05, 0.05):
        L.esfera(0.014, (x, -0.255, 0.25), 'escuro')                             # olhos
        L.esfera(0.022, (x, -0.17, 0.28), 'madeira_escura', escala=(1, 0.6, 1))   # orelhas


L.principal(__file__, construir)
