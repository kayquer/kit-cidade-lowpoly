"""Parquinho: piso de areia com borda de madeira, escorregador (escada, plataforma com telhadinho e rampa
amarela) e balanço de dois assentos."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((1.5, 1.0, 0.025), (0, 0, 0), 'areia')
    for (tam, pos) in (((1.54, 0.04, 0.05), (0, -0.5, 0)), ((1.54, 0.04, 0.05), (0, 0.5, 0)),
                       ((0.04, 1.0, 0.05), (-0.75, 0, 0)), ((0.04, 1.0, 0.05), (0.75, 0, 0))):
        L.caixa(tam, pos, 'madeira', chanfro=0.006)
    # Escorregador (à esquerda): plataforma com 4 colunas, escada atrás, rampa para a frente
    px, py, h = -0.4, 0.15, 0.36
    for dx in (-0.1, 0.1):
        for dy in (-0.1, 0.1):
            L.caixa((0.03, 0.03, 0.56), (px + dx, py + dy, 0.025), 'vermelho')
    L.caixa((0.24, 0.24, 0.03), (px, py, h), 'madeira', chanfro=0.006)
    L.telhado(0.22, 0.22, 0.1, (px, py, 0.58), 'telhado_azul', beiral=0.03)
    for dx in (-0.06, 0.06):
        L.cano((px + dx, py + 0.38, 0.025), (px + dx, py + 0.12, h + 0.03), 0.01, 'metal', lados=4)
    for i in range(4):
        t = (i + 1) / 5
        L.cano((px - 0.06, py + 0.38 - 0.26 * t, 0.025 + h * t), (px + 0.06, py + 0.38 - 0.26 * t, 0.025 + h * t),
               0.008, 'metal', lados=4)
    L.caixa((0.16, 0.62, 0.02), (px, py - 0.4, 0.2), 'amarelo', rot=(34, 0, 0))
    for dx in (-0.08, 0.08):
        L.caixa((0.015, 0.62, 0.04), (px + dx, py - 0.4, 0.21), 'amarelo', rot=(34, 0, 0))
    # Balanço (à direita): pórtico em A e dois assentos
    bx, by = 0.38, 0.05
    for dx in (-0.28, 0.28):
        L.cano((bx + dx, by - 0.18, 0.025), (bx + dx, by, 0.62), 0.016, 'telhado_azul', lados=5)
        L.cano((bx + dx, by + 0.18, 0.025), (bx + dx, by, 0.62), 0.016, 'telhado_azul', lados=5)
    L.cano((bx - 0.3, by, 0.62), (bx + 0.3, by, 0.62), 0.016, 'telhado_azul', lados=5)
    for dx in (-0.12, 0.12):
        for ex in (-0.05, 0.05):
            L.cano((bx + dx + ex, by, 0.62), (bx + dx + ex, by, 0.2), 0.004, 'metal', lados=3)
        L.caixa((0.13, 0.06, 0.015), (bx + dx, by, 0.19), 'vermelho', chanfro=0.004)


L.principal(__file__, construir)
