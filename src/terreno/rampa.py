"""Rampa de terreno (tile 2×2): sobe da altura do chão (z 0) na borda -Y até a altura do morro (z 0,6) na borda
+Y; laterais em terra e pedra e topo de grama inclinado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402
import lib_ruas as R  # noqa: E402

TOPO = 0.6


def construir():
    g = R.GRAMA
    # Perfis (y, z) estendidos ao longo de X. A camada de pedra é uma cunha: some na borda -Y (casa com o tile
    # de grama) e chega a z 0,2 na borda +Y (casa com o morro).
    L.prisma([(-1, R.BASE), (1, R.BASE), (1, 0.2)], 2, (0, 0, 0), 'pedra', eixo='X')
    L.prisma([(-1, R.BASE), (1, 0.2), (1, TOPO - g), (-1, -g)], 2, (0, 0, 0), 'terra', eixo='X')
    L.prisma([(-1, -g), (1, TOPO - g), (1, TOPO), (-1, 0)], 2, (0, 0, 0), 'grama', eixo='X')
    R.capim(0.5, -0.4, 0.1, 0.12)
    R.capim(-0.6, 0.2, 0.1, 0.36)


L.principal(__file__, construir)
