"""Caixa-d'Água Elevada (1×1): estilo cidade do interior — torre de concreto em quatro pilares com vigas
cruzadas, escada marinheiro, tanque cilíndrico branco com faixa azul e borda, tampa cônica, cano de descida
até o registro no chão, cerca e grama em volta."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.08
    L.caixa((1.1, 1.1, 0.06), (0, 0.05, piso), 'concreto', chanfro=0.01)
    z0 = piso + 0.06

    # Quatro pilares com vigas em três níveis
    H = 1.6
    s = 0.36
    for (dx, dy) in ((-s, -s), (s, -s), (-s, s), (s, s)):
        L.caixa((0.11, 0.11, H), (dx, 0.05 + dy, z0), 'concreto', chanfro=0.01)
    for z in (0.5, 1.05):
        L.caixa((2 * s + 0.11, 0.07, 0.07), (0, 0.05 - s, z0 + z), 'concreto')
        L.caixa((2 * s + 0.11, 0.07, 0.07), (0, 0.05 + s, z0 + z), 'concreto')
        L.caixa((0.07, 2 * s + 0.11, 0.07), (-s, 0.05, z0 + z), 'concreto')
        L.caixa((0.07, 2 * s + 0.11, 0.07), (s, 0.05, z0 + z), 'concreto')
    # Laje de apoio
    L.caixa((1.05, 1.05, 0.08), (0, 0.05, z0 + H), 'concreto_escuro', chanfro=0.01)

    # Tanque branco com faixa azul, borda e tampa cônica
    tz = z0 + H + 0.08
    L.cilindro(0.55, 0.7, (0, 0.05, tz), 'parede', lados=12, chanfro=0.015)
    L.cilindro(0.56, 0.12, (0, 0.05, tz + 0.28), 'cano', lados=12)
    L.anel(0.6, 0.5, 0.05, (0, 0.05, tz + 0.7), 'metal', lados=12)
    L.cilindro(0.55, 0.22, (0, 0.05, tz + 0.7), 'telhado_azul', lados=12, r_topo=0.1)
    L.cilindro(0.1, 0.06, (0, 0.05, tz + 0.92), 'metal_escuro', lados=6)                 # respiro
    # Guarda-corpo em volta do topo
    for i in range(8):
        a = 2 * math.pi * i / 8
        x, y = 0.6 * math.cos(a), 0.05 + 0.6 * math.sin(a)
        L.cano((x, y, tz + 0.7), (x, y, tz + 0.9), 0.008, 'metal', lados=4)

    # Escada marinheiro no pilar da frente direita, com gaiola simples
    ex, ey = s + 0.09, 0.05 - s
    L.cano((ex, ey - 0.06, z0), (ex, ey - 0.06, tz + 0.7), 0.01, 'metal', lados=4)
    L.cano((ex, ey + 0.06, z0), (ex, ey + 0.06, tz + 0.7), 0.01, 'metal', lados=4)
    for i in range(14):
        z = z0 + 0.12 + i * 0.16
        L.cano((ex, ey - 0.06, z), (ex, ey + 0.06, z), 0.006, 'metal', lados=4)

    # Cano de descida e registro
    L.cano((-0.2, 0.05, tz), (-0.2, 0.05, z0), 0.04, 'cano', lados=6)
    L.cano((-0.2, 0.05, z0 + 0.1), (-0.2, -0.6, z0 + 0.1), 0.04, 'cano', lados=6)
    L.cilindro(0.06, 0.08, (-0.2, -0.45, z0 + 0.14), 'vermelho', lados=6)                 # registro

    L.cerca(-0.85, -0.8, 0.85, 0.9, alt=0.2, cor='metal')
    L.arbusto((0.65, -0.62, piso), 0.12, 'verde')
    L.arbusto((-0.65, 0.7, piso), 0.12, 'folha')


L.principal(__file__, construir)
