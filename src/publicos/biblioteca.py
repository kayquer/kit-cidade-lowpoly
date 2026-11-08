"""Biblioteca Pública (1×1): prédio creme de fachada clássica com escadaria, quatro colunas, frontão, janelas
altas em arco nas laterais, lanterna de vidro no telhado e jardim com bancos e árvores."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((2.0, 2.0, 0.08), (0, 0, 0), 'grama', chanfro=0.02)
    piso = 0.08
    L.caixa((0.6, 0.55, 0.03), (0, -0.7, piso), 'piso')                    # caminho até a escada

    # Corpo do prédio sobre embasamento
    bx, by, w, d, h = 0.0, 0.35, 1.5, 1.05, 0.95
    L.caixa((w + 0.1, d + 0.1, 0.12), (bx, by, piso), 'pedra', chanfro=0.01)
    pz = piso + 0.12
    L.caixa((w, d, h), (bx, by, pz), 'creme', chanfro=0.025)
    L.caixa((w + 0.06, d + 0.06, 0.08), (bx, by, pz + h), 'parede')        # cornija
    L.telhado4(w, d, 0.28, (bx, by, pz + h + 0.08), 'telhado_vermelho', beiral=0.05)
    # Lanterna de vidro no topo (claraboia)
    L.caixa((0.36, 0.36, 0.2), (bx, by, pz + h + 0.22), 'vidro', chanfro=0.01)
    L.telhado4(0.36, 0.36, 0.12, (bx, by, pz + h + 0.42), 'metal_escuro', beiral=0.03)

    frente = by - d / 2
    # Janelas altas em arco nas laterais da fachada e no lado direito
    for x in (-0.55, 0.55):
        L.placa(0.2, 0.5, (x, frente, pz + 0.65), 'vidro_escuro', 'frente')
        L.cilindro(0.1, 0.03, (x, frente - 0.015, pz + 0.65), 'vidro_escuro', lados=8, rot=(90, 0, 0))
        L.placa(0.26, 0.04, (x, frente - 0.01, pz + 0.17), 'parede', 'frente')
    for y in (by - 0.3, by, by + 0.3):
        L.placa(0.17, 0.5, (bx + w / 2, y, pz + 0.65), 'vidro_escuro', 'direita')
        L.cilindro(0.085, 0.03, (bx + w / 2 + 0.015, y, pz + 0.65), 'vidro_escuro', lados=8, rot=(0, 90, 0))

    # Pórtico: escadaria, colunas, entablamento e frontão
    for i, (lw, ly) in enumerate(((1.0, 0.5), (0.9, 0.4), (0.8, 0.3))):
        L.caixa((lw, ly, 0.05), (0, frente - ly / 2 + 0.02, piso + 0.02 + i * 0.05), 'parede')
    for x in (-0.33, -0.11, 0.11, 0.33):
        L.cilindro(0.045, 0.62, (x, frente - 0.18, pz + 0.05), 'parede', lados=8)
        L.caixa((0.11, 0.11, 0.04), (x, frente - 0.18, pz + 0.05), 'parede')
    L.caixa((0.86, 0.3, 0.08), (0, frente - 0.12, pz + 0.67), 'parede')
    L.prisma([(-0.45, 0), (0.45, 0), (0, 0.22)], 0.3, (0, frente - 0.12, pz + 0.75), 'parede', eixo='Y')
    L.prisma([(-0.32, 0.03), (0.32, 0.03), (0, 0.16)], 0.02, (0, frente - 0.275, pz + 0.75), 'telhado_azul',
             eixo='Y')
    L.placa(0.24, 0.42, (0, frente, pz + 0.47), 'madeira_escura', 'frente')

    # Jardim: bancos, árvores e canteiros
    for x in (-0.65, 0.65):
        L.caixa((0.32, 0.1, 0.07), (x, -0.75, piso), 'madeira')
        L.arbusto((x, -0.45, piso), 0.12, 'verde')
    L.arvore((-0.82, -0.25, piso), 0.65, 'verde')
    L.arvore((0.85, -0.3, piso), 0.6, 'verde_escuro')


L.principal(__file__, construir)
