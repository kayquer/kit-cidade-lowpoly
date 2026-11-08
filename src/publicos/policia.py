"""Delegacia / Base da Polícia (1×1): prédio branco com faixa azul, entrada com marquise azul, giroflex azul e
vermelho no telhado com antena, viatura estilizada (branca e azul) na vaga da frente e cerca baixa."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def viatura(x, y, z):
    """Carro simples branco com faixa azul e giroflex, de frente para -Y."""
    for wx in (-0.17, 0.17):
        for wy in (-0.22, 0.22):
            L.cilindro(0.075, 0.06, (x + wx - 0.03 * (1 if wx > 0 else -1), y + wy, z + 0.075), 'escuro', lados=8,
                       rot=(0, 90, 0))
    L.caixa((0.38, 0.7, 0.16), (x, y, z + 0.05), 'parede', chanfro=0.03)
    L.caixa((0.39, 0.5, 0.05), (x, y, z + 0.1), 'telhado_azul')
    L.caixa((0.32, 0.38, 0.13), (x, y + 0.04, z + 0.21), 'parede', chanfro=0.025)
    L.caixa((0.33, 0.3, 0.08), (x, y + 0.04, z + 0.24), 'vidro_escuro')
    L.caixa((0.14, 0.06, 0.04), (x - 0.04, y + 0.04, z + 0.34), 'telhado_azul')
    L.caixa((0.14, 0.06, 0.04), (x + 0.1, y + 0.04, z + 0.34), 'vermelho')


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.14
    L.caixa((1.9, 1.9, 0.06), (0, 0, 0.08), 'piso')
    L.caixa((0.6, 0.85, 0.008), (0.6, -0.5, piso), 'asfalto')                 # vaga
    L.caixa((0.04, 0.85, 0.004), (0.32, -0.5, piso + 0.008), 'parede')
    L.caixa((0.04, 0.85, 0.004), (0.88, -0.5, piso + 0.008), 'parede')

    # Prédio: branco com faixa azul larga e platibanda azul
    bx, by, w, d, h = -0.25, 0.3, 1.3, 1.1, 1.0
    L.caixa((w, d, h), (bx, by, piso), 'parede', chanfro=0.03)
    L.caixa((w + 0.03, d + 0.03, 0.14), (bx, by, piso + 0.48), 'telhado_azul')
    L.caixa((w + 0.06, d + 0.06, 0.07), (bx, by, piso + h), 'telhado_azul')
    frente = by - d / 2
    # Entrada com porta de vidro e marquise
    L.placa(0.32, 0.4, (bx - 0.2, frente, piso + 0.4), 'vidro_escuro', 'frente')
    L.caixa((0.55, 0.3, 0.04), (bx - 0.2, frente - 0.13, piso + 0.44), 'telhado_azul', chanfro=0.01)
    L.cano((bx - 0.44, frente - 0.26, piso), (bx - 0.44, frente - 0.26, piso + 0.44), 0.015, 'metal', lados=4)
    L.cano((bx + 0.04, frente - 0.26, piso), (bx + 0.04, frente - 0.26, piso + 0.44), 0.015, 'metal', lados=4)
    L.caixa((0.18, 0.02, 0.18), (bx + 0.3, frente - 0.01, piso + 0.22), 'dourado')   # brasão genérico
    # Janelas
    L.janelas('frente', frente, piso + 0.8, bx - 0.5, bx + 0.5, 4, 0.18, 0.2)
    L.janelas('direita', bx + w / 2, piso + 0.28, by - 0.35, by + 0.35, 2, 0.24, 0.22)
    L.janelas('direita', bx + w / 2, piso + 0.8, by - 0.35, by + 0.35, 2, 0.24, 0.2)
    # Giroflex e antena no telhado
    tz = piso + h + 0.07
    L.caixa((0.3, 0.12, 0.05), (bx, by, tz), 'metal_escuro')
    L.caixa((0.12, 0.1, 0.06), (bx - 0.07, by, tz + 0.05), 'telhado_azul')
    L.caixa((0.12, 0.1, 0.06), (bx + 0.07, by, tz + 0.05), 'vermelho')
    L.cano((bx + 0.45, by + 0.3, tz), (bx + 0.45, by + 0.3, tz + 0.6), 0.012, 'metal', lados=4)
    L.cano((bx + 0.38, by + 0.3, tz + 0.45), (bx + 0.52, by + 0.3, tz + 0.45), 0.008, 'metal', lados=4)

    viatura(0.6, -0.5, piso)
    L.cerca(-0.95, -0.95, 0.95, 0.95, alt=0.16, cor='metal_escuro', postes=False)
    L.arbusto((-0.75, -0.75, piso), 0.12, 'verde')


L.principal(__file__, construir)
