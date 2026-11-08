"""Barco de pesca pequeno a motor sobre um pedaço de água: casco branco com faixa azul e popa reta, cabine
pequena com janelas, motor de popa escuro, caixa de isopor e vara de pesca."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def casco(meia, larg, z, h, cor):
    """Contorno visto de cima: proa pontuda em -Y, popa reta em +Y; extrudado de z até z + h."""
    lado = []
    for i in range(7):
        t = i / 6                                    # 0 = proa, 1 = popa
        lado.append((larg * min(1.0, (t * 1.6) ** 0.55), -meia + 2 * meia * t))
    perfil = lado + [(-x, y) for (x, y) in reversed(lado[1:])]
    return L.prisma(perfil, h, (0, 0, z), cor, eixo='Z')


def construir():
    L.cilindro(0.85, 0.02, (0, 0, 0), 'agua', lados=12)
    casco(0.62, 0.2, 0.0, 0.07, 'telhado_azul')
    casco(0.66, 0.24, 0.07, 0.08, 'parede')
    casco(0.58, 0.2, 0.145, 0.008, 'madeira')                         # piso interno
    # Cabine
    L.caixa((0.3, 0.26, 0.2), (0, -0.05, 0.15), 'parede', chanfro=0.012)
    L.caixa((0.26, 0.012, 0.08), (0, -0.185, 0.25), 'vidro')
    L.caixa((0.012, 0.18, 0.07), (0.153, -0.05, 0.25), 'vidro')
    L.caixa((0.34, 0.3, 0.025), (0, -0.05, 0.35), 'telhado_azul', chanfro=0.008)
    # Motor de popa
    L.caixa((0.1, 0.1, 0.13), (0, 0.66, 0.12), 'escuro', chanfro=0.015)
    L.caixa((0.035, 0.03, 0.18), (0, 0.69, -0.04), 'metal_escuro')
    # Caixa de isopor e vara
    L.caixa((0.14, 0.1, 0.08), (0.07, 0.35, 0.153), 'parede', chanfro=0.01)
    L.cano((-0.15, 0.4, 0.16), (-0.25, -0.1, 0.55), 0.006, 'escuro', lados=4)


L.principal(__file__, construir)
