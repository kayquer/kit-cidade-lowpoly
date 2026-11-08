"""
Reescreve o catálogo dos READMEs (entre <!-- catalogo:inicio --> e <!-- catalogo:fim -->) a partir de
models/catalogo.json, que o src/gerar_todos.py grava. Rodar com Python 3 comum (não precisa do Blender):

    py -3 tools/atualizar_readme.py

- README.md (inglês, principal): nomes de tools/nomes_en.json (todo modelo novo precisa de uma entrada lá).
- README.pt-BR.md (português): primeira frase da docstring de cada script.
Também regrava a lista de modelos do llms.txt (entre as mesmas marcas).
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIAS = [
    ('residencial', 'Residencial', 'Residential'),
    ('comercial', 'Comércio', 'Commercial'),
    ('publicos', 'Serviços públicos', 'Public services'),
    ('industrial', 'Indústria', 'Industry'),
    ('agua', 'Água e saneamento', 'Water and sanitation'),
    ('energia', 'Energia', 'Energy'),
    ('residuos', 'Resíduos', 'Waste and recycling'),
    ('parques', 'Parques', 'Parks'),
    ('ruas', 'Ruas (peças modulares 2 × 2)', 'Roads (modular 2 × 2 tiles)'),
    ('terreno', 'Terreno (peças modulares 2 × 2)', 'Terrain (modular 2 × 2 tiles)'),
    ('veiculos', 'Veículos', 'Vehicles'),
    ('mobiliario', 'Mobiliário urbano', 'Street furniture'),
    ('vegetacao', 'Vegetação', 'Vegetation'),
    ('beira_rio', 'Beira-rio', 'Riverside'),
]

TEXTOS = {
    'en': {'arquivo': 'README.md', 'total': '**{n} models** in {c} categories.',
           'cabecalho': ['| | Model | Description | Tris |', '|---|---|---|---:|'], 'img': 'Low poly {en} 3D models'},
    'pt': {'arquivo': 'README.pt-BR.md', 'total': '**{n} modelos** em {c} categorias.',
           'cabecalho': ['| | Modelo | Descrição | Tris |', '|---|---|---|---:|'], 'img': 'Modelos 3D low poly: {pt}'},
}


def resumo(descricao):
    """Primeira frase da docstring, sem o tamanho em lotes repetido."""
    frase = re.split(r'(?<=[.:])\s', descricao, maxsplit=1)[0].rstrip('.:')
    return frase.replace('|', '/')


def substituir(caminho, linhas):
    texto = open(caminho, encoding='utf-8').read()
    novo = re.sub(r'(<!-- catalogo:inicio -->\n).*?(<!-- catalogo:fim -->)',
                  lambda m: m.group(1) + '\n'.join(linhas) + '\n' + m.group(2), texto, flags=re.S)
    open(caminho, 'w', encoding='utf-8', newline='\n').write(novo)


def main():
    catalogo = json.load(open(os.path.join(RAIZ, 'models', 'catalogo.json'), encoding='utf-8'))
    nomes_en = json.load(open(os.path.join(RAIZ, 'tools', 'nomes_en.json'), encoding='utf-8'))
    faltando = sorted(set(catalogo) - set(nomes_en))
    if faltando:
        sys.exit('Sem nome em inglês em tools/nomes_en.json: ' + ', '.join(faltando))
    por_cat = {}
    for m in catalogo.values():
        por_cat.setdefault(m['categoria'], []).append(m)
    conhecidas = [c for c, _, _ in CATEGORIAS]
    extras = [(c, c.capitalize(), c) for c in sorted(por_cat) if c not in conhecidas]
    total = sum(len(v) for v in por_cat.values())

    for lingua, t in TEXTOS.items():
        linhas = [t['total'].format(n=total, c=len(por_cat)), '']
        for cat, pt, en in CATEGORIAS + extras:
            itens = sorted(por_cat.get(cat, []), key=lambda m: m['id'])
            if not itens:
                continue
            titulo = f'{en} · {pt}' if lingua == 'en' else f'{pt} · {en}'
            linhas += [f'### {titulo} ({len(itens)})', '']
            if os.path.exists(os.path.join(RAIZ, 'previews', cat + '.jpg')):
                linhas += [f'![{t["img"].format(en=en.split(" (")[0].lower(), pt=pt)}](previews/{cat}.jpg)', '']
            linhas += t['cabecalho']
            for m in itens:
                chave = f'{cat}/{m["id"]}'
                desc = nomes_en[chave] if lingua == 'en' else resumo(m['descricao'])
                mini = f'previews/{cat}/{m["id"]}.jpg'
                img = (f'<img src="{mini}" width="120" alt="{desc.replace(chr(34), "")}">'
                       if os.path.exists(os.path.join(RAIZ, mini)) else '')
                linhas.append(f'| {img} | [`{m["id"]}`](models/{chave}.glb) | {desc} | {m["tris"]} |')
            linhas.append('')
        substituir(os.path.join(RAIZ, t['arquivo']), linhas)

    # llms.txt: lista compacta, um modelo por linha
    llms = os.path.join(RAIZ, 'llms.txt')
    if os.path.exists(llms):
        linhas = []
        for cat, pt, en in CATEGORIAS + extras:
            itens = sorted(por_cat.get(cat, []), key=lambda m: m['id'])
            if itens:
                linhas.append(f'- {en} ({pt}): ' + '; '.join(
                    f'`models/{cat}/{m["id"]}.glb` {nomes_en[cat + "/" + m["id"]]}' for m in itens))
        substituir(llms, linhas)
    print('READMEs atualizados:', total, 'modelos')


if __name__ == '__main__':
    main()
