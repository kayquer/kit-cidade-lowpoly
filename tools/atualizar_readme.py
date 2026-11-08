"""
Reescreve o catálogo do README (entre <!-- catalogo:inicio --> e <!-- catalogo:fim -->) a partir de
models/catalogo.json, que o src/gerar_todos.py grava. Rodar com Python 3 comum (não precisa do Blender):

    py -3 tools/atualizar_readme.py
"""
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(RAIZ, 'README.md')

CATEGORIAS = [
    ('residencial', 'Residencial', 'Residential'),
    ('comercial', 'Comércio', 'Commercial'),
    ('publicos', 'Serviços públicos', 'Public services'),
    ('industrial', 'Indústria', 'Industry'),
    ('agua', 'Água e saneamento', 'Water and sanitation'),
    ('energia', 'Energia', 'Energy'),
    ('residuos', 'Resíduos', 'Waste'),
    ('parques', 'Parques', 'Parks'),
    ('ruas', 'Ruas (peças modulares 2 × 2)', 'Roads (modular 2 × 2 tiles)'),
    ('terreno', 'Terreno (peças modulares 2 × 2)', 'Terrain (modular 2 × 2 tiles)'),
    ('veiculos', 'Veículos', 'Vehicles'),
    ('mobiliario', 'Mobiliário urbano', 'Street furniture'),
    ('vegetacao', 'Vegetação', 'Vegetation'),
    ('beira_rio', 'Beira-rio', 'Riverside'),
]


def resumo(descricao):
    """Primeira frase da docstring, sem o tamanho em lotes repetido."""
    frase = re.split(r'(?<=[.:])\s', descricao, maxsplit=1)[0].rstrip('.:')
    return frase.replace('|', '/')


def main():
    catalogo = json.load(open(os.path.join(RAIZ, 'models', 'catalogo.json'), encoding='utf-8'))
    por_cat = {}
    for m in catalogo.values():
        por_cat.setdefault(m['categoria'], []).append(m)
    conhecidas = [c for c, _, _ in CATEGORIAS]
    extras = [(c, c.capitalize(), c) for c in sorted(por_cat) if c not in conhecidas]

    total = sum(len(v) for v in por_cat.values())
    linhas = [f'**{total} modelos** em {len(por_cat)} categorias.', '']
    for cat, pt, en in CATEGORIAS + extras:
        itens = sorted(por_cat.get(cat, []), key=lambda m: m['id'])
        if not itens:
            continue
        linhas += [f'### {pt} · {en} ({len(itens)})', '']
        if os.path.exists(os.path.join(RAIZ, 'previews', cat + '.jpg')):
            linhas += [f'![{pt}](previews/{cat}.jpg)', '']
        linhas += ['| | Modelo | Descrição | Tris |', '|---|---|---|---:|']
        for m in itens:
            mini = f'previews/{cat}/{m["id"]}.jpg'
            img = f'<img src="{mini}" width="120">' if os.path.exists(os.path.join(RAIZ, mini)) else ''
            linhas.append(f'| {img} | [`{m["id"]}`](models/{cat}/{m["id"]}.glb) | {resumo(m["descricao"])} | {m["tris"]} |')
        linhas.append('')

    texto = open(README, encoding='utf-8').read()
    novo = re.sub(r'(<!-- catalogo:inicio -->\n).*?(<!-- catalogo:fim -->)',
                  lambda m: m.group(1) + '\n'.join(linhas) + '\n' + m.group(2), texto, flags=re.S)
    open(README, 'w', encoding='utf-8', newline='\n').write(novo)
    print('README atualizado:', total, 'modelos')


if __name__ == '__main__':
    main()
