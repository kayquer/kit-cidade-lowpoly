"""Casas geminadas (1×1): duas casinhas térreas coladas, uma amarela-clara e outra rosa, cada uma com seu
telhado de duas águas de frente para a rua, porta colorida, janela, jardinzinho e lixeira na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def casinha(cx, cor, telha, porta, flor):
    piso = 0.08
    cy, larg, prof, alt = 0.25, 0.82, 1.1, 0.55
    L.caixa((larg, prof, alt), (cx, cy, piso), cor, chanfro=0.015)
    L.caixa((larg + 0.02, prof + 0.02, 0.04), (cx, cy, piso), 'concreto_escuro')
    L.telhado(larg, prof, 0.36, (cx, cy, piso + alt), telha, beiral=0.06, eixo='Y')
    frente = cy - prof / 2
    L.placa(0.18, 0.36, (cx - 0.18, frente, piso + 0.18), porta, 'frente')
    L.janelas('frente', frente, piso + 0.32, cx + 0.05, cx + 0.3, 1, 0.22, 0.2, moldura='parede')
    L.placa(0.12, 0.12, (cx, frente - 0.01, piso + 0.72), 'parede', 'frente')      # óculo no oitão
    L.placa(0.08, 0.08, (cx, frente - 0.02, piso + 0.72), 'vidro', 'frente')
    # Jardinzinho e mureta
    L.caixa((0.82, 0.04, 0.1), (cx, -0.88, piso), 'parede', chanfro=0.006)
    L.arbusto((cx + 0.2, -0.55, piso), 0.1, 'verde')
    L.esfera(0.025, (cx + 0.22, -0.62, piso + 0.12), flor)
    L.caixa((0.2, 0.55, 0.015), (cx - 0.18, -0.6, piso), 'piso')


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    casinha(-0.42, 'creme', 'telhado_vermelho', 'telhado_azul', 'flor_rosa')
    casinha(0.42, 'flor_rosa', 'telhado_vermelho', 'verde_escuro', 'flor_amarela')
    L.janelas('direita', 0.83, 0.42, 0.0, 0.5, 2, 0.18, 0.2, moldura='parede')
    # Lixeirinha e poste de luz na calçada
    L.cilindro(0.05, 0.14, (0.75, -0.75, 0.08), 'verde_escuro', lados=6)
    L.cano((-0.85, -0.82, 0.08), (-0.85, -0.82, 0.85), 0.015, 'metal_escuro', lados=5)
    L.esfera(0.04, (-0.85, -0.82, 0.88), 'flor_amarela')


L.principal(__file__, construir)
