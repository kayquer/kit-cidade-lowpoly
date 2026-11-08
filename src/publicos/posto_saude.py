"""Posto de Saúde / UBS (1×1): prédio térreo branco com faixa verde e cruz verde na fachada, entrada com
marquise, rampa de acessibilidade com corrimão, bancos de espera, ambulância simples e jardim."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def cruz(x, y, z, t, face='frente'):
    if face == 'frente':
        L.placa(t, t * 0.34, (x, y, z), 'verde', 'frente', espessura=0.02)
        L.placa(t * 0.34, t, (x, y, z), 'verde', 'frente', espessura=0.02)
    else:
        L.placa(t, t * 0.34, (x, y, z), 'verde', 'direita', espessura=0.02)
        L.placa(t * 0.34, t, (x, y, z), 'verde', 'direita', espessura=0.02)


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    base = 0.08
    L.caixa((1.9, 0.5, 0.04), (0, -0.7, base), 'piso')                       # calçada da frente
    piso = base + 0.16                                                       # prédio sobre uma laje elevada
    bx, by, w, d, h = 0.0, 0.3, 1.7, 1.05, 0.62
    L.caixa((w + 0.1, d + 0.1, 0.16), (bx, by, base), 'concreto', chanfro=0.01)
    L.caixa((w, d, h), (bx, by, piso), 'parede', chanfro=0.03)
    L.caixa((w + 0.03, d + 0.03, 0.07), (bx, by, piso), 'verde')
    L.caixa((w + 0.08, d + 0.08, 0.06), (bx, by, piso + h), 'creme')
    L.caixa((w - 0.2, d - 0.2, 0.04), (bx, by, piso + h + 0.06), 'concreto_escuro')
    L.caixa((0.3, 0.3, 0.2), (0.5, by + 0.15, piso + h + 0.1), 'cano', chanfro=0.015)        # caixa-d'água
    L.caixa((0.2, 0.2, 0.06), (-0.4, by + 0.2, piso + h + 0.1), 'metal')                       # ar-condicionado
    frente = by - d / 2
    # Entrada: porta de vidro e marquise verde
    L.placa(0.36, 0.38, (-0.35, frente, piso + 0.38), 'vidro', 'frente')
    L.caixa((0.6, 0.32, 0.04), (-0.35, frente - 0.14, piso + 0.42), 'verde', chanfro=0.01)
    # Cruz verde na fachada e no lado direito
    cruz(0.45, frente - 0.01, piso + 0.45, 0.26)
    cruz(bx + w / 2 + 0.01, by, piso + 0.45, 0.26, face='direita')
    L.janelas('frente', frente, piso + 0.2, 0.1, 0.8, 3, 0.16, 0.14)
    L.janelas('direita', bx + w / 2, piso + 0.18, by - 0.4, by + 0.4, 3, 0.16, 0.14)

    # Rampa de acessibilidade (sobe da calçada à laje pela esquerda) com corrimão
    ry = frente - 0.2
    L.prisma([(-0.75, 0), (-0.15, 0), (-0.15, 0.16)], 0.26, (0, ry, base), 'concreto', eixo='Y')
    L.cano((-0.75, ry - 0.13, base + 0.16), (-0.15, ry - 0.13, piso + 0.16), 0.01, 'metal', lados=4)
    L.cano((-0.75, ry - 0.13, base), (-0.75, ry - 0.13, base + 0.16), 0.01, 'metal', lados=4)
    L.cano((-0.15, ry - 0.13, base + 0.16), (-0.15, ry - 0.13, piso + 0.16), 0.01, 'metal', lados=4)
    L.caixa((0.3, 0.26, 0.16), (0.0, ry, base), 'concreto')                 # patamar
    L.caixa((0.3, 0.06, 0.003), (0.0, ry - 0.1, piso), 'amarelo')            # piso tátil

    # Ambulância simples (branca com faixa vermelha) e bancos
    ax, ay = 0.55, -0.65
    for wx in (-0.14, 0.14):
        for wy in (-0.18, 0.2):
            L.cilindro(0.06, 0.05, (ax + wx + (0.025 if wx > 0 else -0.025), ay + wy, base + 0.1), 'escuro', lados=8,
                       rot=(0, 90, 0))
    L.caixa((0.32, 0.6, 0.27), (ax, ay, base + 0.06), 'parede', chanfro=0.025)
    L.caixa((0.33, 0.6, 0.04), (ax, ay, base + 0.17), 'vermelho')
    L.caixa((0.3, 0.12, 0.1), (ax, ay - 0.25, base + 0.2), 'vidro_escuro')
    L.caixa((0.1, 0.06, 0.04), (ax, ay - 0.15, base + 0.33), 'vermelho')
    L.caixa((0.3, 0.09, 0.07), (-0.75, 0.0, base), 'madeira')
    L.arbusto((-0.8, -0.85, base), 0.11, 'verde')
    L.arbusto((0.85, 0.9, base), 0.13, 'folha')


L.principal(__file__, construir)
