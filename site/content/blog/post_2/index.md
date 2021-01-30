---
title: "2 - Pesquisa automatizada no Pubmed"
date: "2020-12-20T00:00:00.000Z"
description: "No âmbito do trabalho surgiu a necessidade de obter de forma sistémica um resumo da literatura disponível sobre os diferentes genes/proteínas em estudo."
categories: [Revisão Bibliográfica, Scripts]
---

No âmbito do trabalho surgiu a necessidade de obter de forma sistémica um resumo da literatura disponível sobre os diferentes genes/proteínas em estudo.

Esta ferramenta foi então desenvolvida de forma a permitir fazer variações de cada pesquisa, por ex: funções de um gene, ou associações a uma patologia.

## Definição de critérios de pesquisa

Definimos os termos a pesquisar como os 3 diferentes genes escolhidos pelo grupo, e para cada um procurar artigos que foquem em aspetos genéricos, função e associação à patologia *Sars-Cov_2*.


```python
search_keywords = ["generic", "function", "sars-cov-2"]
genes = ["21_ORF7a", "22_BST2", "23_ITGAL"]
```

## Modulo *'pubmed.py'*

### *search_articles()* - Pesquisa de artigos

Este método vai itenerar sobre a lista de *search_keywords* adicionando-as ao termo mãe, que no nosso caso são os genes, à exceção de *generic* que pesquisa unicamente o termo mãe.

Em termos de critérios de filtragem a função permite mudar por exemplo em que materiais a pesquisa é feita (titulos, nomes de autores, etc) sendo o nosso default 'WORD' e 'TIAB', além de 'LANG' para a lingua inglesa.
Filtra também o contéudo aos ultimos cinco anos e organiza por "Best Match"

Internamente cada pesquisa devolve uma lista dos 20 primeiros resultados, sendo que as pesquisas no fim agregadas pelo seu código PMID, marcadas as *search_keywords* em que a pesquisa devolveu este artigo. agregando assim os duplicados.


```python
from scripts_python.pubmed import search_articles

result = search_articles("21_ORF7a", search_keywords)

for PMID in result.keys():
    print(PMID, ": ", result[PMID])
```

    33305306 :  {'search_keywords': ['generic']}
    33227343 :  {'search_keywords': ['generic', 'sars-cov-2']}
    33195401 :  {'search_keywords': ['generic', 'sars-cov-2']}
    33163695 :  {'search_keywords': ['generic', 'sars-cov-2']}
    33161087 :  {'search_keywords': ['generic', 'sars-cov-2']}
    33024967 :  {'search_keywords': ['generic', 'function', 'sars-cov-2']}
    32971122 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32935103 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32929412 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32869027 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32814791 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32773420 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32754056 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32713862 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32691005 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32623351 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32615316 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32547891 :  {'search_keywords': ['generic', 'function', 'sars-cov-2']}
    32511591 :  {'search_keywords': ['generic', 'sars-cov-2']}
    32511297 :  {'search_keywords': ['generic', 'sars-cov-2']}
    26378163 :  {'search_keywords': ['function']}
    23054027 :  {'search_keywords': ['function']}
    16328780 :  {'search_keywords': ['function']}
    15740663 :  {'search_keywords': ['function']}
    15642263 :  {'search_keywords': ['function']}
    32357959 :  {'search_keywords': ['sars-cov-2']}


### *fetch_article()* - Recolha de artigos

Depois de identificados os PMID dos diferentes artigos foi necessário criar um método que devolvesse o contéudo necessário destes.

Este devolve um dicionário com o título, endereço web do artigo e abstract.


```python
from scripts_python.pubmed import fetch_article

result = fetch_article(33305306)

for key in result.keys():
    print(key, ": ", result[key])
```

    title :  Structural assessment of SARS-CoV2 accessory protein ORF7a predicts LFA-1 and Mac-1 binding potential.
    web_address :  https://pubmed.ncbi.nlm.nih.gov/33305306/
    abstract :  ORF7a is an accessory protein common to SARS-CoV1 and the recently discovered SARS-CoV2, which is causing the COVID19 pandemic. The ORF7a protein has a structural homology with ICAM-1 which binds to the T lymphocyte integrin receptor LFA-1. As COVID19 has a strong immune component as part of the disease, we sought to determine whether SARS-CoV2 would have a similar structural interaction with LFA-1. Using molecular docking simulations, we found that SARS-CoV2 ORF7a has the key structural determinants required to bind LFA-1 but also the related leukocyte integrin Mac-1, which is also known to be expressed by macrophages. Our study shows that SARS-CoV2 ORF7a protein has a conserved Ig immunoglobulin-like fold containing an integrin binding site that provides a mechanistic hypothesis for SARS-CoV2's interaction with the human immune system. This suggests that experimental investigation of ORF7a mediated effects on immune cells such as T lymphocytes and macrophages (leukocytes) could help understand the disease further and develop effective treatments.


### *search_fetch_articles()* - Agregação de informações dos artigos para uma pesquisa

Com base nos dois métodos anteriormente desenvolvidos, foi então possível criar um único que permitisse tanto pesquisar como recolher os dados.

Esta percorre a estrutura de dados devolvida pela *search_articles()* e adiciona para cada *PMID* os restantes dados obtidos pela *fetch_article()*.


```python
from scripts_python.pubmed import search_fetch_articles

result = search_fetch_articles("21_ORF7a", search_keywords)

# Primeiro Artigo
for key in result['33305306'].keys():
    print(key, ": ", result['33305306'][key])

# Nº de artigos
print(len(result))

```

    search_keywords :  ['generic']
    title :  Structural assessment of SARS-CoV2 accessory protein ORF7a predicts LFA-1 and Mac-1 binding potential.
    web_address :  https://pubmed.ncbi.nlm.nih.gov/33305306/
    abstract :  ORF7a is an accessory protein common to SARS-CoV1 and the recently discovered SARS-CoV2, which is causing the COVID19 pandemic. The ORF7a protein has a structural homology with ICAM-1 which binds to the T lymphocyte integrin receptor LFA-1. As COVID19 has a strong immune component as part of the disease, we sought to determine whether SARS-CoV2 would have a similar structural interaction with LFA-1. Using molecular docking simulations, we found that SARS-CoV2 ORF7a has the key structural determinants required to bind LFA-1 but also the related leukocyte integrin Mac-1, which is also known to be expressed by macrophages. Our study shows that SARS-CoV2 ORF7a protein has a conserved Ig immunoglobulin-like fold containing an integrin binding site that provides a mechanistic hypothesis for SARS-CoV2's interaction with the human immune system. This suggests that experimental investigation of ORF7a mediated effects on immune cells such as T lymphocytes and macrophages (leukocytes) could help understand the disease further and develop effective treatments.
    26


### *search_print_articles()* - Agregação e Arquivo de informações dos artigos para uma pesquisa

Este método corre o *search_fetch_articles()* e faz output de um ficheiros de *markdown* na diretoria escolhida. Isto permite um arquivo para uma certa data dos resultados. Por esta razão a fução cria também uma *time stamp* no nome do ficheiro.


```python
from scripts_python.pubmed import search_print_articles

result = search_print_articles("21_ORF7a", search_keywords, file="../scripts_python/tests_data/{0}_search_results.md".format("21_ORF7a"))
```

    ../scripts/tests_data/ORF7a_search_results_2020-12-21.md


## Resultados

O método *search_print_articles()* pode ser então itenerado para todos os nossos genes de interesse, produzindo um conjunto de ficheiros com o output das diferentes pesquisas feitas para cada gene.

Estes podem ser consultados em [Resultados](https://github.com/DiogoM1/MBINF_LB_projeto/tree/main/data).


```python
for gene in genes:
    search_print_articles(search_term=gene, search_keywords=search_keywords, file="../data/{0}_search_results.md".format(gene))



```

    ../data/ORF7a_search_results_2020-12-21.md
    ../data/BST2_search_results_2020-12-21.md
    ../data/ITGAL_search_results_2020-12-21.md

