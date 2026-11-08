"""Caminhão-pipa: cabine branca, tanque cilíndrico azul deitado com faixas, escotilha e passarela no topo,
registro traseiro com mangueira e dois eixos traseiros."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import _veiculos as V  # noqa: E402

LARG = 0.5


def construir():
    V.chassi(LARG, -0.66, 0.7)
    V.cabine_caminhao('parede', LARG, y_frente=-0.7, comp=0.36)
    L.caixa((LARG - 0.1, 0.95, 0.04), (0, 0.2, 0.1), 'metal_escuro')                   # berço
    # Tanque: cilindro deitado (rot X 90 → eixo para -Y; a base fica na traseira)
    L.cilindro(0.21, 0.95, (0, 0.68, 0.35), 'agua_funda', lados=12, rot=(90, 0, 0), chanfro=0.02)
    for y in (-0.08, 0.2, 0.48):
        L.cilindro(0.218, 0.03, (0, y + 0.015, 0.35), 'parede', lados=12, rot=(90, 0, 0))   # aros
    L.cilindro(0.05, 0.03, (0, 0.2, 0.55), 'metal', lados=8)                            # escotilha
    L.caixa((0.12, 0.7, 0.012), (0, 0.2, 0.56), 'metal_escuro')                        # passarela
    L.cano((0, 0.68, 0.2), (0, 0.76, 0.2), 0.03, 'metal', lados=6)                     # registro
    L.cilindro(0.04, 0.03, (-0.15, 0.7, 0.12), 'escuro', lados=8, rot=(90, 0, 0))     # mangueira
    V.lanternas(LARG, 0.7, 0.08)
    V.rodas(LARG, (-0.5, 0.38, 0.58), r=0.09)


L.principal(__file__, construir)
