"""Posto de recarga de carros elétricos (1×1): cobertura de painéis solares sobre duas vagas com
carregadores verdes, faixas de vaga pintadas, lojinha de conveniência envidraçada, bateria estacionária
e canteiros."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def carregador(x, y, z):
    L.caixa((0.12, 0.08, 0.3), (x, y, z), 'parede', chanfro=0.01)
    L.placa(0.08, 0.07, (x, y - 0.04, z + 0.22), 'vidro_escuro', 'frente', espessura=0.01)
    L.placa(0.08, 0.02, (x, y - 0.045, z + 0.12), 'verde', 'frente', espessura=0.01)
    L.cano((x + 0.06, y - 0.02, z + 0.15), (x + 0.12, y - 0.1, z + 0.02), 0.008, 'escuro', lados=4)


def construir():
    L.caixa((1.9, 1.9, 0.08), (0, 0, 0), 'asfalto', chanfro=0.02)
    piso = 0.08
    # Vagas com piso verde
    for x in (-0.55, 0.05):
        L.caixa((0.5, 0.95, 0.005), (x, -0.3, piso), 'verde')
        L.caixa((0.05, 0.95, 0.006), (x - 0.27, -0.3, piso), 'parede')
    L.caixa((0.05, 0.95, 0.006), (0.33, -0.3, piso), 'parede')
    # Ilha com os carregadores
    L.caixa((1.3, 0.2, 0.05), (-0.25, 0.27, piso), 'concreto', chanfro=0.01)
    carregador(-0.55, 0.27, piso + 0.05)
    carregador(0.05, 0.27, piso + 0.05)
    # Cobertura solar
    for x in (-0.85, 0.35):
        L.caixa((0.06, 0.06, 0.8), (x, 0.3, piso), 'metal_escuro')
    L.caixa((1.45, 1.1, 0.05), (-0.25, -0.05, piso + 0.8), 'metal', rot=(-8, 0, 0), chanfro=0.01)
    for i in range(3):
        for j in range(2):
            L.caixa((0.42, 0.48, 0.015), (-0.73 + i * 0.48, -0.3 + j * 0.52, piso + 0.85 - (j - 0.5) * 0.0),
                    'painel_solar', rot=(-8, 0, 0))
    # Lojinha de conveniência à direita
    sx, sy = 0.7, 0.45
    L.caixa((0.42, 0.8, 0.5), (sx, sy, piso), 'parede', chanfro=0.015)
    L.caixa((0.48, 0.86, 0.05), (sx, sy, piso + 0.5), 'telhado_verde')
    L.placa(0.3, 0.32, (sx, sy - 0.4, piso + 0.2), 'vidro', 'frente')
    L.placa(0.6, 0.3, (sx + 0.21, sy, piso + 0.22), 'vidro', 'direita')
    # Bateria estacionária
    L.caixa((0.2, 0.3, 0.3), (0.75, -0.55, piso), 'metal', chanfro=0.01)
    L.placa(0.12, 0.04, (0.85, -0.55, piso + 0.24), 'amarelo', 'direita', espessura=0.01)
    # Canteiros
    L.caixa((0.4, 0.15, 0.06), (-0.6, -0.87, piso), 'grama')
    L.arbusto((-0.7, -0.87, piso + 0.06), 0.08, 'verde')
    L.arbusto((-0.5, -0.87, piso + 0.06), 0.07, 'folha')


L.principal(__file__, construir)
