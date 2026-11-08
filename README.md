# Kit Cidade Low Poly

![Kit Cidade Low Poly](previews/capa.jpg)

Modelos 3D low poly **livres** para montar cidades: casas, comércio, serviços públicos, água e saneamento,
energia, resíduos, parques, ruas e terreno modulares, veículos, mobiliário urbano, vegetação nativa brasileira
e beira de rio. Tudo em **glTF binário (`.glb`)**, com cores chapadas e sem texturas, pronto para Godot, Unity,
Unreal, Babylon.js, three.js, Blender e afins.

**Domínio público ([CC0 1.0](LICENSE)).** Use como quiser, em projetos pessoais, educativos ou comerciais,
modifique e redistribua. Dar crédito é opcional (veja [CITATION.cff](CITATION.cff)). Sem nenhuma garantia.

> **English:** free low poly city kit — houses, shops, public services, water and sanitation, energy, waste,
> parks, modular roads and terrain, vehicles, street furniture, Brazilian native trees and riverside props.
> Flat-colored `.glb` files, no textures. **Public domain (CC0 1.0)**: use it for anything, commercial
> included; attribution is optional; no warranty. File and category names are in Portuguese (see the table
> headers for the English category names).

## Como usar

- Baixe o repositório (botão **Code → Download ZIP**) ou só os `.glb` de que precisar em [`models/`](models).
- **Escala e grade:** 1 lote = 2 × 2 unidades. Prédios ocupam N × N lotes; ruas e terreno são peças de
  exatamente 2 × 2 que se encaixam lado a lado; veículos, props e mobiliário estão numa escala "de brinquedo"
  que conversa com esses lotes.
- **Orientação:** Y para cima, frente dos modelos voltada para **-Z** (convenção glTF).
- **Materiais:** um material por cor (PBR, só cor base, rugosidade 0,85). Para juntar tudo num draw call,
  converta as cores dos materiais em cor de vértice na sua engine.
- **Partes animáveis:** objetos chamados `pas_N` (rotores, giram no eixo do cubo) e `gira_N` (giram em pé)
  ficam separados do corpo, com o pivô no lugar.
- **Orçamento:** no máximo 1.500 triângulos e 150 KB por modelo.

### Ruas e terreno modulares

As peças de `ruas/` e `terreno/` ocupam exatamente x, z ∈ [-1, 1] e se encaixam numa grade de 2 unidades,
girando em múltiplos de 90° em Y. Medidas em glTF (Y para cima):

| Elemento | Medida |
|---|---|
| Bloco de terreno | de y -0,3 a 0 (topo da grama em 0); as ruas já trazem o bloco embaixo e **substituem** o tile de terreno |
| Asfalto | 1,3 de largura centrada (\|x\| ≤ 0,65), topo em y 0,04, faixa amarela tracejada no eixo |
| Meio-fio e calçada | meio-fio com topo em 0,075; calçada de \|x\| 0,65 a 1,0 com topo em 0,07 |
| Estrada de terra | mesma largura do asfalto, topo em y 0,02, sem calçada |
| Água | superfície em y -0,12; margem de areia em degrau a y -0,06 |
| Morro | topo em y 0,6; `rampa` sobe de 0 (borda -Z) a 0,6 (borda +Z) |

Conexões sem rotação: `asfalto_reta`, `asfalto_faixa_pedestre`, `terra_reta` e `ponte` ligam -Z e +Z;
`asfalto_curva` e `terra_curva` ligam -Z e -X; `asfalto_t` liga -Z, +Z e -X; `asfalto_ponta` só -Z;
`estacionamento` abre para -Z; `margem_reta` tem a água na metade -Z; `margem_canto` tem a água num quarto de
círculo no canto (+X, -Z). Veja um bairro montado em [`src/cena_cidade.py`](src/cena_cidade.py).

## Catálogo

<!-- catalogo:inicio -->
**129 modelos** em 14 categorias.

### Residencial · Residential (5)

![Residencial](previews/residencial.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/residencial/casa_simples.jpg" width="120"> | [`casa_simples`](models/residencial/casa_simples.glb) | Casa simples (1×1) | 584 |
| <img src="previews/residencial/casa_sobrado.jpg" width="120"> | [`casa_sobrado`](models/residencial/casa_sobrado.glb) | Sobrado (1×1) | 564 |
| <img src="previews/residencial/casas_geminadas.jpg" width="120"> | [`casas_geminadas`](models/residencial/casas_geminadas.glb) | Casas geminadas (1×1) | 588 |
| <img src="previews/residencial/predio_alto.jpg" width="120"> | [`predio_alto`](models/residencial/predio_alto.glb) | Prédio alto residencial (1×1) | 1008 |
| <img src="previews/residencial/predio_apartamentos.jpg" width="120"> | [`predio_apartamentos`](models/residencial/predio_apartamentos.glb) | Prédio de apartamentos (1×1) | 1208 |

### Comércio · Commercial (8)

![Comércio](previews/comercial.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/comercial/banco.jpg" width="120"> | [`banco`](models/comercial/banco.glb) | Agência bancária (1×1) | 662 |
| <img src="previews/comercial/escritorio.jpg" width="120"> | [`escritorio`](models/comercial/escritorio.glb) | Prédio de escritórios (1×1) | 820 |
| <img src="previews/comercial/hotel.jpg" width="120"> | [`hotel`](models/comercial/hotel.glb) | Hotel (1×1) | 678 |
| <img src="previews/comercial/loja_esquina.jpg" width="120"> | [`loja_esquina`](models/comercial/loja_esquina.glb) | Loja de esquina (1×1) | 652 |
| <img src="previews/comercial/mercado.jpg" width="120"> | [`mercado`](models/comercial/mercado.glb) | Mercado de bairro (1×1) | 512 |
| <img src="previews/comercial/posto_recarga.jpg" width="120"> | [`posto_recarga`](models/comercial/posto_recarga.glb) | Posto de recarga de carros elétricos (1×1) | 636 |
| <img src="previews/comercial/restaurante.jpg" width="120"> | [`restaurante`](models/comercial/restaurante.glb) | Restaurante (1×1) | 738 |
| <img src="previews/comercial/shopping.jpg" width="120"> | [`shopping`](models/comercial/shopping.glb) | Shopping (2×2) | 796 |

### Serviços públicos · Public services (12)

![Serviços públicos](previews/publicos.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/publicos/biblioteca.jpg" width="120"> | [`biblioteca`](models/publicos/biblioteca.glb) | Biblioteca Pública (1×1) | 812 |
| <img src="previews/publicos/bombeiros.jpg" width="120"> | [`bombeiros`](models/publicos/bombeiros.glb) | Corpo de Bombeiros (1×1) | 670 |
| <img src="previews/publicos/centro_pesquisa.jpg" width="120"> | [`centro_pesquisa`](models/publicos/centro_pesquisa.glb) | Centro de Pesquisa (2×2) | 952 |
| <img src="previews/publicos/centro_tecnologia.jpg" width="120"> | [`centro_tecnologia`](models/publicos/centro_tecnologia.glb) | Centro de Tecnologia (1×1) | 686 |
| <img src="previews/publicos/escola.jpg" width="120"> | [`escola`](models/publicos/escola.glb) | Escola (2×2) | 1328 |
| <img src="previews/publicos/hospital.jpg" width="120"> | [`hospital`](models/publicos/hospital.glb) | Hospital (2×2) | 1224 |
| <img src="previews/publicos/monumento.jpg" width="120"> | [`monumento`](models/publicos/monumento.glb) | Monumento Histórico (2×2) | 1154 |
| <img src="previews/publicos/museu.jpg" width="120"> | [`museu`](models/publicos/museu.glb) | Museu (3×3) | 1238 |
| <img src="previews/publicos/policia.jpg" width="120"> | [`policia`](models/publicos/policia.glb) | Delegacia / Base da Polícia (1×1) | 772 |
| <img src="previews/publicos/posto_saude.jpg" width="120"> | [`posto_saude`](models/publicos/posto_saude.glb) | Posto de Saúde / UBS (1×1) | 724 |
| <img src="previews/publicos/prefeitura.jpg" width="120"> | [`prefeitura`](models/publicos/prefeitura.glb) | Prefeitura Municipal (2×2) | 1146 |
| <img src="previews/publicos/universidade.jpg" width="120"> | [`universidade`](models/publicos/universidade.glb) | Universidade (3×3) | 1352 |

### Indústria · Industry (4)

![Indústria](previews/industrial.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/industrial/fabrica.jpg" width="120"> | [`fabrica`](models/industrial/fabrica.glb) | Fábrica (2×2) | 1372 |
| <img src="previews/industrial/galpao.jpg" width="120"> | [`galpao`](models/industrial/galpao.glb) | Galpão / Armazém (1×1) | 748 |
| <img src="previews/industrial/oficina.jpg" width="120"> | [`oficina`](models/industrial/oficina.glb) | Oficina Mecânica (1×1) | 1164 |
| <img src="previews/industrial/porto.jpg" width="120"> | [`porto`](models/industrial/porto.glb) | Porto (2×2, sobre a água) | 1020 |

### Água e saneamento · Water and sanitation (16)

![Água e saneamento](previews/agua.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/agua/barragem_subterranea.jpg" width="120"> | [`barragem_subterranea`](models/agua/barragem_subterranea.glb) | Barragem Subterrânea (2×2) | 592 |
| <img src="previews/agua/bomba_agua.jpg" width="120"> | [`bomba_agua`](models/agua/bomba_agua.glb) | Bomba de Água (1×1) | 440 |
| <img src="previews/agua/caixa_dagua.jpg" width="120"> | [`caixa_dagua`](models/agua/caixa_dagua.glb) | Caixa-d'Água Elevada (1×1) | 1232 |
| <img src="previews/agua/centro_controle_perdas.jpg" width="120"> | [`centro_controle_perdas`](models/agua/centro_controle_perdas.glb) | Centro de Controle de Perdas (2×2) | 964 |
| <img src="previews/agua/centro_pesquisa_agua.jpg" width="120"> | [`centro_pesquisa_agua`](models/agua/centro_pesquisa_agua.glb) | Centro de Pesquisas Hídricas (3×3) | 1112 |
| <img src="previews/agua/estacao_filtragem.jpg" width="120"> | [`estacao_filtragem`](models/agua/estacao_filtragem.glb) | Estação de Filtros (1×1) | 984 |
| <img src="previews/agua/estacao_monitoramento.jpg" width="120"> | [`estacao_monitoramento`](models/agua/estacao_monitoramento.glb) | Estação de Monitoramento (1×1) | 684 |
| <img src="previews/agua/eta.jpg" width="120"> | [`eta`](models/agua/eta.glb) | Estação de Tratamento de Água — ETA (2×2) | 1268 |
| <img src="previews/agua/ete.jpg" width="120"> | [`ete`](models/agua/ete.glb) | Estação de Tratamento de Esgoto — ETE (2×2) | 1232 |
| <img src="previews/agua/jardim_chuva.jpg" width="120"> | [`jardim_chuva`](models/agua/jardim_chuva.glb) | Jardim de Chuva (2×2) | 776 |
| <img src="previews/agua/jardim_flutuante.jpg" width="120"> | [`jardim_flutuante`](models/agua/jardim_flutuante.glb) | Jardim Flutuante (3×3, sobre a água) | 1212 |
| <img src="previews/agua/monitor_qualidade_agua.jpg" width="120"> | [`monitor_qualidade_agua`](models/agua/monitor_qualidade_agua.glb) | Monitor de Qualidade (1×1) | 508 |
| <img src="previews/agua/poco_artesiano.jpg" width="120"> | [`poco_artesiano`](models/agua/poco_artesiano.glb) | Poço Artesiano (1×1) | 656 |
| <img src="previews/agua/reservatorio.jpg" width="120"> | [`reservatorio`](models/agua/reservatorio.glb) | Reservatório (1×1) | 868 |
| <img src="previews/agua/usina_dessalinizacao.jpg" width="120"> | [`usina_dessalinizacao`](models/agua/usina_dessalinizacao.glb) | Usina de Dessalinização (3×3) | 1468 |
| <img src="previews/agua/usina_reuso_agua.jpg" width="120"> | [`usina_reuso_agua`](models/agua/usina_reuso_agua.glb) | Estação de Água de Reúso (3×3) | 938 |

### Energia · Energy (11)

![Energia](previews/energia.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/energia/biodigestor.jpg" width="120"> | [`biodigestor`](models/energia/biodigestor.glb) | Biodigestor (2×2) | 1408 |
| <img src="previews/energia/hidreletrica.jpg" width="120"> | [`hidreletrica`](models/energia/hidreletrica.glb) | Hidrelétrica (3×3, sobre a água) | 972 |
| <img src="previews/energia/parque_eolico.jpg" width="120"> | [`parque_eolico`](models/energia/parque_eolico.glb) | Campo Eólico (2×2) | 846 |
| <img src="previews/energia/poste_energia.jpg" width="120"> | [`poste_energia`](models/energia/poste_energia.glb) | Poste de Energia (1×1) | 264 |
| <img src="previews/energia/termeletrica.jpg" width="120"> | [`termeletrica`](models/energia/termeletrica.glb) | Termelétrica (2×2) | 844 |
| <img src="previews/energia/usina_biomassa.jpg" width="120"> | [`usina_biomassa`](models/energia/usina_biomassa.glb) | Usina de Biomassa (2×2) | 1056 |
| <img src="previews/energia/usina_cana.jpg" width="120"> | [`usina_cana`](models/energia/usina_cana.glb) | Usina Sucroenergética (3×3) | 1440 |
| <img src="previews/energia/usina_carvao.jpg" width="120"> | [`usina_carvao`](models/energia/usina_carvao.glb) | Usina a Carvão (2×2) | 512 |
| <img src="previews/energia/usina_mare.jpg" width="120"> | [`usina_mare`](models/energia/usina_mare.glb) | Usina Maremotriz (2×2, sobre a água) | 640 |
| <img src="previews/energia/usina_nuclear.jpg" width="120"> | [`usina_nuclear`](models/energia/usina_nuclear.glb) | Usina Nuclear (4×4) | 1488 |
| <img src="previews/energia/usina_solar.jpg" width="120"> | [`usina_solar`](models/energia/usina_solar.glb) | Usina Solar (3×3) | 944 |

### Resíduos · Waste (4)

![Resíduos](previews/residuos.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/residuos/aterro_sanitario.jpg" width="120"> | [`aterro_sanitario`](models/residuos/aterro_sanitario.glb) | Aterro Sanitário (3×3) | 1482 |
| <img src="previews/residuos/cooperativa_reciclagem.jpg" width="120"> | [`cooperativa_reciclagem`](models/residuos/cooperativa_reciclagem.glb) | Cooperativa de Reciclagem (2×2) | 1302 |
| <img src="previews/residuos/patio_compostagem.jpg" width="120"> | [`patio_compostagem`](models/residuos/patio_compostagem.glb) | Pátio de Compostagem (2×2) | 1158 |
| <img src="previews/residuos/ponto_coleta.jpg" width="120"> | [`ponto_coleta`](models/residuos/ponto_coleta.glb) | Ponto de Coleta Reciclável / PEV (1×1) | 832 |

### Parques · Parks (5)

![Parques](previews/parques.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/parques/ecoparque.jpg" width="120"> | [`ecoparque`](models/parques/ecoparque.glb) | Ecoparque (3×3) | 1480 |
| <img src="previews/parques/parede_verde.jpg" width="120"> | [`parede_verde`](models/parques/parede_verde.glb) | Parede Verde (1×1) | 876 |
| <img src="previews/parques/parque.jpg" width="120"> | [`parque`](models/parques/parque.glb) | Parque Turístico (4×4) | 1484 |
| <img src="previews/parques/parque_linear.jpg" width="120"> | [`parque_linear`](models/parques/parque_linear.glb) | Parque Linear (3×3) | 900 |
| <img src="previews/parques/telhado_verde.jpg" width="120"> | [`telhado_verde`](models/parques/telhado_verde.glb) | Teto Verde (2×2) | 1332 |

### Ruas (peças modulares 2 × 2) · Roads (modular 2 × 2 tiles) (12)

![Ruas (peças modulares 2 × 2)](previews/ruas.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/ruas/asfalto_cruzamento.jpg" width="120"> | [`asfalto_cruzamento`](models/ruas/asfalto_cruzamento.glb) | Cruzamento de asfalto (tile 2×2) | 492 |
| <img src="previews/ruas/asfalto_curva.jpg" width="120"> | [`asfalto_curva`](models/ruas/asfalto_curva.glb) | Rua de asfalto em curva (tile 2×2) | 548 |
| <img src="previews/ruas/asfalto_faixa_pedestre.jpg" width="120"> | [`asfalto_faixa_pedestre`](models/ruas/asfalto_faixa_pedestre.glb) | Rua de asfalto reta com faixa de pedestres (tile 2×2) | 228 |
| <img src="previews/ruas/asfalto_ponta.jpg" width="120"> | [`asfalto_ponta`](models/ruas/asfalto_ponta.glb) | Fim de rua com balão de retorno (tile 2×2) | 524 |
| <img src="previews/ruas/asfalto_reta.jpg" width="120"> | [`asfalto_reta`](models/ruas/asfalto_reta.glb) | Rua de asfalto reta (tile 2×2) | 132 |
| <img src="previews/ruas/asfalto_t.jpg" width="120"> | [`asfalto_t`](models/ruas/asfalto_t.glb) | Entroncamento em T de asfalto (tile 2×2) | 264 |
| <img src="previews/ruas/calcada.jpg" width="120"> | [`calcada`](models/ruas/calcada.glb) | Calçada (tile 2×2) | 108 |
| <img src="previews/ruas/estacionamento.jpg" width="120"> | [`estacionamento`](models/ruas/estacionamento.glb) | Estacionamento (tile 2×2) | 320 |
| <img src="previews/ruas/ponte.jpg" width="120"> | [`ponte`](models/ruas/ponte.glb) | Ponte de concreto (tile 2×2, substitui um tile de água) | 428 |
| <img src="previews/ruas/praca.jpg" width="120"> | [`praca`](models/ruas/praca.glb) | Praça (tile 2×2) | 496 |
| <img src="previews/ruas/terra_curva.jpg" width="120"> | [`terra_curva`](models/ruas/terra_curva.glb) | Estrada de terra em curva (tile 2×2) | 484 |
| <img src="previews/ruas/terra_reta.jpg" width="120"> | [`terra_reta`](models/ruas/terra_reta.glb) | Estrada de terra reta (tile 2×2) | 160 |

### Terreno (peças modulares 2 × 2) · Terrain (modular 2 × 2 tiles) (9)

![Terreno (peças modulares 2 × 2)](previews/terreno.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/terreno/agua.jpg" width="120"> | [`agua`](models/terreno/agua.glb) | Água (tile 2×2) | 48 |
| <img src="previews/terreno/areia.jpg" width="120"> | [`areia`](models/terreno/areia.glb) | Terreno de areia (tile 2×2) | 90 |
| <img src="previews/terreno/arvores_mata.jpg" width="120"> | [`arvores_mata`](models/terreno/arvores_mata.glb) | Mata (tile 2×2) | 208 |
| <img src="previews/terreno/grama.jpg" width="120"> | [`grama`](models/terreno/grama.glb) | Terreno de grama (tile 2×2) | 24 |
| <img src="previews/terreno/margem_canto.jpg" width="120"> | [`margem_canto`](models/terreno/margem_canto.glb) | Margem em canto (tile 2×2) | 320 |
| <img src="previews/terreno/margem_reta.jpg" width="120"> | [`margem_reta`](models/terreno/margem_reta.glb) | Margem reta de rio (tile 2×2) | 148 |
| <img src="previews/terreno/morro.jpg" width="120"> | [`morro`](models/terreno/morro.glb) | Morro (tile 2×2) | 108 |
| <img src="previews/terreno/rampa.jpg" width="120"> | [`rampa`](models/terreno/rampa.glb) | Rampa de terreno (tile 2×2) | 56 |
| <img src="previews/terreno/terra.jpg" width="120"> | [`terra`](models/terreno/terra.glb) | Terreno de terra batida (tile 2×2) | 144 |

### Veículos · Vehicles (10)

![Veículos](previews/veiculos.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/veiculos/ambulancia.jpg" width="120"> | [`ambulancia`](models/veiculos/ambulancia.glb) | Ambulância (furgão) | 624 |
| <img src="previews/veiculos/bicicleta.jpg" width="120"> | [`bicicleta`](models/veiculos/bicicleta.glb) | Bicicleta solta | 332 |
| <img src="previews/veiculos/caminhao.jpg" width="120"> | [`caminhao`](models/veiculos/caminhao.glb) | Caminhão baú | 676 |
| <img src="previews/veiculos/caminhao_bombeiros.jpg" width="120"> | [`caminhao_bombeiros`](models/veiculos/caminhao_bombeiros.glb) | Caminhão de bombeiros | 1028 |
| <img src="previews/veiculos/caminhao_lixo.jpg" width="120"> | [`caminhao_lixo`](models/veiculos/caminhao_lixo.glb) | Caminhão de lixo (coletor compactador) | 616 |
| <img src="previews/veiculos/caminhao_pipa.jpg" width="120"> | [`caminhao_pipa`](models/veiculos/caminhao_pipa.glb) | Caminhão-pipa | 856 |
| <img src="previews/veiculos/carro.jpg" width="120"> | [`carro`](models/veiculos/carro.glb) | Carro hatch vermelho | 464 |
| <img src="previews/veiculos/carro_eletrico.jpg" width="120"> | [`carro_eletrico`](models/veiculos/carro_eletrico.glb) | Carro elétrico | 488 |
| <img src="previews/veiculos/onibus.jpg" width="120"> | [`onibus`](models/veiculos/onibus.glb) | Ônibus urbano | 616 |
| <img src="previews/veiculos/taxi.jpg" width="120"> | [`taxi`](models/veiculos/taxi.glb) | Táxi | 520 |

### Mobiliário urbano · Street furniture (20)

![Mobiliário urbano](previews/mobiliario.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/mobiliario/banco_praca.jpg" width="120"> | [`banco_praca`](models/mobiliario/banco_praca.glb) | Banco de praça | 420 |
| <img src="previews/mobiliario/barril_chuva.jpg" width="120"> | [`barril_chuva`](models/mobiliario/barril_chuva.glb) | Barril de captação de chuva | 672 |
| <img src="previews/mobiliario/bebedouro.jpg" width="120"> | [`bebedouro`](models/mobiliario/bebedouro.glb) | Bebedouro público | 472 |
| <img src="previews/mobiliario/bicicletario.jpg" width="120"> | [`bicicletario`](models/mobiliario/bicicletario.glb) | Bicicletário | 476 |
| <img src="previews/mobiliario/cerca_madeira.jpg" width="120"> | [`cerca_madeira`](models/mobiliario/cerca_madeira.glb) | Cerca de madeira (trecho de 2 unidades ao longo de X) | 348 |
| <img src="previews/mobiliario/cisterna.jpg" width="120"> | [`cisterna`](models/mobiliario/cisterna.glb) | Cisterna de placas (semiárido) | 600 |
| <img src="previews/mobiliario/hidrante.jpg" width="120"> | [`hidrante`](models/mobiliario/hidrante.glb) | Hidrante de rua | 422 |
| <img src="previews/mobiliario/lixeira.jpg" width="120"> | [`lixeira`](models/mobiliario/lixeira.glb) | Lixeira comum de calçada (papeleira) | 284 |
| <img src="previews/mobiliario/lixeira_seletiva.jpg" width="120"> | [`lixeira_seletiva`](models/mobiliario/lixeira_seletiva.glb) | Lixeira seletiva de rua | 936 |
| <img src="previews/mobiliario/orelhao.jpg" width="120"> | [`orelhao`](models/mobiliario/orelhao.glb) | Orelhão (telefone público brasileiro) | 276 |
| <img src="previews/mobiliario/parquinho.jpg" width="120"> | [`parquinho`](models/mobiliario/parquinho.glb) | Parquinho | 596 |
| <img src="previews/mobiliario/placa_educativa.jpg" width="120"> | [`placa_educativa`](models/mobiliario/placa_educativa.glb) | Placa educativa de beira de rio | 274 |
| <img src="previews/mobiliario/placa_pare.jpg" width="120"> | [`placa_pare`](models/mobiliario/placa_pare.glb) | Placa de parada obrigatória | 136 |
| <img src="previews/mobiliario/ponto_onibus.jpg" width="120"> | [`ponto_onibus`](models/mobiliario/ponto_onibus.glb) | Ponto de ônibus com telhado verde | 480 |
| <img src="previews/mobiliario/poste_luz.jpg" width="120"> | [`poste_luz`](models/mobiliario/poste_luz.glb) | Poste de iluminação comum | 236 |
| <img src="previews/mobiliario/poste_solar.jpg" width="120"> | [`poste_solar`](models/mobiliario/poste_solar.glb) | Poste solar | 320 |
| <img src="previews/mobiliario/quiosque.jpg" width="120"> | [`quiosque`](models/mobiliario/quiosque.glb) | Quiosque de praça | 462 |
| <img src="previews/mobiliario/semaforo.jpg" width="120"> | [`semaforo`](models/mobiliario/semaforo.glb) | Semáforo veicular de esquina | 480 |
| <img src="previews/mobiliario/semaforo_pedestre.jpg" width="120"> | [`semaforo_pedestre`](models/mobiliario/semaforo_pedestre.glb) | Semáforo de pedestre | 212 |
| <img src="previews/mobiliario/vaso_planta.jpg" width="120"> | [`vaso_planta`](models/mobiliario/vaso_planta.glb) | Floreira de concreto de calçada | 328 |

### Vegetação · Vegetation (7)

![Vegetação](previews/vegetacao.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/vegetacao/araucaria.jpg" width="120"> | [`araucaria`](models/vegetacao/araucaria.glb) | Araucária (pinheiro-do-paraná) | 548 |
| <img src="previews/vegetacao/arbustos.jpg" width="120"> | [`arbustos`](models/vegetacao/arbustos.glb) | Conjunto de arbustos para canteiro | 200 |
| <img src="previews/vegetacao/buriti.jpg" width="120"> | [`buriti`](models/vegetacao/buriti.glb) | Buriti (palmeira das veredas) | 636 |
| <img src="previews/vegetacao/composteira.jpg" width="120"> | [`composteira`](models/vegetacao/composteira.glb) | Composteira de dois módulos de ripas de madeira | 1332 |
| <img src="previews/vegetacao/horta.jpg" width="120"> | [`horta`](models/vegetacao/horta.glb) | Canteiro de horta comunitária | 494 |
| <img src="previews/vegetacao/ipe_amarelo.jpg" width="120"> | [`ipe_amarelo`](models/vegetacao/ipe_amarelo.glb) | Ipê-amarelo (árvore nativa) | 388 |
| <img src="previews/vegetacao/pedras.jpg" width="120"> | [`pedras`](models/vegetacao/pedras.glb) | Conjunto de pedras de beira de rio | 108 |

### Beira-rio · Riverside (6)

![Beira-rio](previews/beira_rio.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/beira_rio/barco_pesca.jpg" width="120"> | [`barco_pesca`](models/beira_rio/barco_pesca.glb) | Barco de pesca pequeno a motor sobre um pedaço de água | 412 |
| <img src="previews/beira_rio/boia_rio.jpg" width="120"> | [`boia_rio`](models/beira_rio/boia_rio.glb) | Boia de monitoramento do rio | 364 |
| <img src="previews/beira_rio/canoa.jpg" width="120"> | [`canoa`](models/beira_rio/canoa.glb) | Canoa de madeira de pescador num remanso do rio | 296 |
| <img src="previews/beira_rio/capivara.jpg" width="120"> | [`capivara`](models/beira_rio/capivara.glb) | Capivara estilizada num pedaço de grama da margem | 300 |
| <img src="previews/beira_rio/garca.jpg" width="120"> | [`garca`](models/beira_rio/garca.glb) | Garça-branca em pé numa pedra da beira do rio | 222 |
| <img src="previews/beira_rio/trapiche.jpg" width="120"> | [`trapiche`](models/beira_rio/trapiche.glb) | Trapiche (píer curto de madeira) | 570 |

<!-- catalogo:fim -->

## Como gerar ou modificar

Cada modelo é um script Python em `src/<categoria>/<id>.py` que usa as peças da biblioteca [`src/lib.py`](src/lib.py)
(caixas, cilindros, canos, telhados, janelas, árvores…) e a paleta de cores única. Precisa do Blender 4.5 LTS.

```bash
blender -b --factory-startup --python src/agua/eta.py                 # um modelo → models/agua/eta.glb
blender -b --factory-startup --python src/gerar_todos.py              # todos (+ models/catalogo.json)
blender -b --factory-startup --python src/gerar_todos.py -- ruas      # só uma categoria
blender -b --factory-startup --python src/vitrine.py -- tudo --cada   # imagens em previews/
blender -b --factory-startup --python src/cena_cidade.py              # previews/capa.jpg (bairro de exemplo)
py -3 tools/atualizar_readme.py                                       # refaz o catálogo acima
```

Para criar um modelo novo: copie um script parecido, monte a peça com a **frente para -Y do Blender** (o
`exportar` gira 180° para a frente ficar em -Z no glTF) e use só cores de `PALETA`.

## Origem e créditos

O kit nasceu dos modelos próprios do jogo educativo [Guardião da Água](https://github.com/kayquer/guardiao_da_agua_js),
produto da pesquisa de mestrado de Cláudia Dias Roxinol (Unesp, Presidente Prudente), desenvolvido com Kayque
Rotondo. Os modelos e scripts foram feitos com o Blender e com o Claude (Anthropic) como assistente. Nenhum modelo
de terceiros faz parte deste repositório.
