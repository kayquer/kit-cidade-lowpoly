"""Placa de parada obrigatória: octógono vermelho com borda branca (sem letras), costas de metal e poste."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.05, 0.02, (0, 0, 0), 'concreto', lados=6)
    L.cilindro(0.018, 0.75, (0, 0, 0.02), 'metal', lados=6)
    # Octógono com lado reto em cima: cilindro de 8 lados deitado (eixo -Y) e girado 22,5° no próprio eixo
    L.cilindro(0.15, 0.012, (0, -0.02, 0.68), 'metal', lados=8, rot=(90, 22.5, 0))
    L.cilindro(0.145, 0.006, (0, -0.032, 0.68), 'parede', lados=8, rot=(90, 22.5, 0))
    L.cilindro(0.128, 0.006, (0, -0.038, 0.68), 'vermelho', lados=8, rot=(90, 22.5, 0))
    L.caixa((0.14, 0.004, 0.03), (0, -0.042, 0.665), 'parede')                # faixa branca (sem texto)


L.principal(__file__, construir)
