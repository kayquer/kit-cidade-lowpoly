"""Galpão / Armazém (1×1): galpão de metal com telhado em arco, portão de enrolar listrado, porta lateral,
plataforma de carga, pilhas de paletes e caixas, empilhadeira amarela e faixas de segurança no pátio."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((2.0, 2.0, 0.06), (0, 0, 0), 'concreto', chanfro=0.02)
    piso = 0.06

    # Corpo do galpão e telhado em arco
    gx, gy, w, d, h = -0.1, 0.35, 1.55, 1.2, 0.7
    L.caixa((w, d, h), (gx, gy, piso), 'metal', chanfro=0.02)
    for i in range(5):                                        # frisos verticais da chapa (lado direito)
        L.caixa((0.015, 0.02, h), (gx + w / 2 + 0.005, gy - d / 2 + 0.15 + i * 0.22, piso), 'metal_escuro')
    arco = []
    for i in range(7):
        a = math.pi * i / 6
        arco.append((-(w / 2 + 0.04) * math.cos(a), 0.35 * math.sin(a)))
    interno = [(x * 0.96, z * 0.8) for (x, z) in reversed(arco)]
    L.prisma(arco + interno, d + 0.08, (gx, gy, piso + h), 'telhado_azul', eixo='Y')
    L.prisma(arco, 0.02, (gx, gy - d / 2 + 0.01, piso + h), 'metal', eixo='Y')     # tímpano da frente
    # Portão de enrolar (listras) e porta de serviço
    frente = gy - d / 2
    L.placa(0.7, 0.55, (gx - 0.25, frente, piso + 0.58), 'metal_escuro', 'frente', espessura=0.02)
    for i in range(6):
        L.placa(0.7, 0.02, (gx - 0.25, frente - 0.02, piso + 0.08 + i * 0.09), 'metal', 'frente', espessura=0.006)
    L.placa(0.18, 0.36, (gx + 0.5, frente, piso + 0.39), 'laranja', 'frente')
    L.janelas('direita', gx + w / 2, piso + 0.55, gy - 0.3, gy + 0.3, 2, 0.24, 0.12)
    # Plataforma de carga com faixa amarela e preta
    L.caixa((0.85, 0.3, 0.12), (gx - 0.25, frente - 0.15, piso), 'concreto_escuro')
    for i in range(5):
        L.caixa((0.08, 0.02, 0.1), (gx - 0.6 + i * 0.18, frente - 0.3, piso + 0.01), 'amarelo', rot=(0, 30, 0))

    # Paletes e caixas
    def palete(x, y, z):
        L.caixa((0.3, 0.3, 0.04), (x, y, z), 'madeira')
        return z + 0.04
    z = palete(0.65, -0.65, piso)
    L.caixa((0.26, 0.26, 0.22), (0.65, -0.65, z), 'cavaco', chanfro=0.01)
    z = palete(0.65, -0.25, piso)
    z = palete(0.65, -0.25, z)
    L.caixa((0.26, 0.26, 0.16), (0.65, -0.25, z), 'laranja', chanfro=0.01)
    palete(0.3, -0.8, piso)
    # Empilhadeira
    ex, ey = -0.6, -0.65
    L.caixa((0.22, 0.32, 0.14), (ex, ey, piso + 0.04), 'amarelo', chanfro=0.02)
    for (wx, wy) in ((-0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (0.1, 0.1)):
        L.cilindro(0.045, 0.04, (ex + wx + (0.02 if wx > 0 else -0.02), ey + wy, piso + 0.045), 'escuro', lados=6,
                   rot=(0, 90, 0))
    L.cano((ex - 0.08, ey + 0.1, piso + 0.18), (ex - 0.08, ey + 0.1, piso + 0.42), 0.01, 'escuro', lados=4)
    L.cano((ex + 0.08, ey + 0.1, piso + 0.18), (ex + 0.08, ey + 0.1, piso + 0.42), 0.01, 'escuro', lados=4)
    L.caixa((0.2, 0.2, 0.02), (ex, ey + 0.1, piso + 0.42), 'escuro')                   # teto de proteção
    L.caixa((0.18, 0.04, 0.36), (ex, ey - 0.18, piso + 0.04), 'metal_escuro')           # torre do garfo
    for gx2 in (-0.05, 0.05):
        L.caixa((0.03, 0.2, 0.015), (ex + gx2, ey - 0.3, piso + 0.06), 'metal_escuro')


L.principal(__file__, construir)
