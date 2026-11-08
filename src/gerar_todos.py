"""
Regera os modelos do kit numa única execução do Blender (cada src/<cat>/<id>.py → models/<cat>/<id>.glb):

    blender -b --factory-startup --python src/gerar_todos.py                 # todas as categorias
    blender -b --factory-startup --python src/gerar_todos.py -- agua ruas    # só estas

No fim imprime a tabela categoria/id → triângulos/KB e grava models/catalogo.json (lido pelo README e pela vitrine).
"""
import glob
import importlib.util
import json
import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(SRC)
sys.path.insert(0, SRC)
import lib as L  # noqa: E402

pedidas = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
categorias = sorted(d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d)) and not d.startswith(('_', '.')))
if pedidas:
    categorias = [c for c in categorias if c in pedidas]

CATALOGO = os.path.join(RAIZ, 'models', 'catalogo.json')
catalogo = json.load(open(CATALOGO, encoding='utf-8')) if os.path.exists(CATALOGO) else {}
erros = []
for cat in categorias:
    for caminho in sorted(glob.glob(os.path.join(SRC, cat, '*.py'))):
        nome = os.path.basename(caminho)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(f'{cat}.{nome}', caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)  # L.principal não gera ao importar
            tris = L.gerar(caminho, modulo.construir)
        except Exception as e:  # noqa: BLE001 - segue com os outros e lista no fim
            erros.append(f'{cat}/{nome}: {e!r}')
            continue
        glb = os.path.join(RAIZ, 'models', cat, nome + '.glb')
        doc = (modulo.__doc__ or '').strip().replace('\n', ' ')
        catalogo[f'{cat}/{nome}'] = {'categoria': cat, 'id': nome, 'tris': tris,
                                     'kb': round(os.path.getsize(glb) / 1024, 1), 'descricao': doc}

catalogo = dict(sorted(catalogo.items()))
with open(CATALOGO, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(catalogo, f, ensure_ascii=False, indent=1)
    f.write('\n')

print('\n' + 'modelo'.ljust(40) + 'tris'.rjust(6) + 'KB'.rjust(8))
for chave, m in catalogo.items():
    if m['categoria'] not in categorias:
        continue
    alerta = '  <-- acima do orçamento' if m['tris'] > 1500 or m['kb'] > 150 else ''
    print(chave.ljust(40) + str(m['tris']).rjust(6) + f"{m['kb']:8.1f}" + alerta)
for e in erros:
    print('ERRO', e)
