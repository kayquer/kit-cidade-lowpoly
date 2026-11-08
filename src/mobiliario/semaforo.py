"""Semáforo veicular de esquina: coluna de metal com braço sobre a rua (-X), grupo focal pendurado no braço
e outro na coluna, cada um com vermelho, amarelo e verde voltados para a frente (-Y)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def grupo(x, y, z):
    """Caixa escura com três luzes e pala, topo em z."""
    L.caixa((0.1, 0.08, 0.3), (x, y, z - 0.3), 'escuro', chanfro=0.01)
    for i, cor in enumerate(('vermelho', 'amarelo', 'verde')):
        zc = z - 0.06 - i * 0.09
        L.cilindro(0.032, 0.012, (x, y - 0.04, zc), cor, lados=8, rot=(90, 0, 0))
        L.caixa((0.08, 0.03, 0.008), (x, y - 0.055, zc + 0.035), 'escuro')   # pala


def construir():
    L.cilindro(0.08, 0.03, (0, 0, 0), 'concreto', lados=8)
    L.cilindro(0.03, 1.35, (0, 0, 0.03), 'metal_escuro', lados=8, r_topo=0.025)
    L.cano((0, 0, 1.3), (-0.9, 0, 1.3), 0.02, 'metal_escuro', lados=6)
    L.cano((0, 0, 1.1), (-0.3, 0, 1.3), 0.012, 'metal_escuro', lados=5)       # mão-francesa
    L.cano((-0.75, 0, 1.3), (-0.75, 0, 1.25), 0.01, 'metal_escuro', lados=5)
    grupo(-0.75, 0, 1.25)
    grupo(0, -0.07, 0.8)
    L.caixa((0.08, 0.05, 0.1), (0.05, 0.03, 0.5), 'metal', chanfro=0.006)     # caixa de controle


L.principal(__file__, construir)
