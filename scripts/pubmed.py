from Bio import Entrez
from datetime import date

Entrez.email = "pedroalex123@gmail.com"

"""
{
'WORD': 'Text Word, Free text associated with publication', 
'LANG': 'Language, Language of publication', 
'TIAB': 'Title/Abstract, Free text associated with Abstract/Title', 
} 
"""

["generic", "function", "Sars-CoV2"]
# Dicionário de listas, em que cada chave corresponde a uma pesquisa "generic", "pathology", "function"


def search_articles(db, search_term, search_keywords=["generic"], search_fields=['WORD', 'TIAB'], time_period=5):
    """
    Pesquisa artigos numa base da dados a especificar, com os termos a especificar
    se quiser pesquisa de "base" usar "generic"
    :param search_keywords:
    :param search_term:
    :param time_period:
    :param search_fields: por título, autor, etc.
    :param db: base de dados a procurar
    :param term: termos a pesquisar
    :return: lista de IDs de artigos
    """
    today = date.today()
    searches = {}

    for key in search_keywords:
        if key == "generic":
            keyword = str(search_term)
        else:
            keyword = "{0} {1}".format(search_term, key)

        query = "("
        for field in range(len(search_fields)):
            if field < len(search_fields)-1:
                query += "({0}[{1}]) OR".format(keyword, search_fields[field])
            else:
                query += "({0}[{1}])".format(keyword, search_fields[field])
            query += ") AND english[LANG]"

        handle = Entrez.esearch(db=str(db), term=query, mindate=today.year - time_period, sort='Best Match')
        record = Entrez.read(handle)
        searches[key] = record["IdList"]

    return searches


def search_fetch_articles(db, search_term, search_keywords=["generic"], search_fields=['WORD', 'TIAB'], time_period=5):
    """
    returns file with cenas
    :param db:
    :param search_term:
    :param search_keywords:
    :param search_fields:
    :param time_period:
    :return:
    """
    for id in id_list:
        handle = Entrez.efetch(db="pubmed", id=str(id), rettype="abstract", retmode="XML")
        record = Entrez.read(handle)
        article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
        title = article["ArticleTitle"]
        doi = record["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][2]
        if "Abstract" in article:
            abstract = article["Abstract"]["AbstractText"][0]
        else:
            abstract = None

        dict = {}

        print(title)

    handle666 = Entrez.efetch(db="pubmed", id=33305306, rettype="abstract", retmode="XML")
    record666 = Entrez.read(handle666)
    print("doi={0}".format(record666["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][2]))
    doi = record666["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][2].attributes["IdType"]

# bst_handle = Entrez.esearch(db="pubmed", term="BST2[TITL]") #procura por artigos que tenham o BST2 no título
# bst_record = Entrez.read(bst_handle)
# print(bst_record["IdList"])


# itgal_handle = Entrez.esearch(db="pubmed", term="ITGAL[TITL]") #procura por artigos que tenham o ITGAL no título
# itgal_record = Entrez.read(itgal_handle)
# print(itgal_record["IdList"])