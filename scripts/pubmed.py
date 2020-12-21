from Bio import Entrez
from datetime import date

from scripts.general import time_stamping

Entrez.email = "pedroalex123@gmail.com"


def search_articles(search_term, search_keywords=["generic"], search_fields=('WORD', 'TIAB'), time_period=5):
    """
    Pesquisa artigos numa base da dados a especificar, com os termos a especificar
    se quiser pesquisa de "base" usar "generic"

    {
    bd_id:
        {
        "search_keywords": [],
        }
    }

    :param search_term: termos a pesquisar
    :param search_keywords:
    :param time_period:
    :param search_fields: por título, autor, etc.
    :return: lista de IDs de artigos
    """
    today = date.today()
    search_results = {}

    for key in search_keywords:
        if key == "generic":
            keyword = str(search_term)
        else:
            keyword = "{0} {1}".format(search_term, key)

        # create pubmed query
        query = ""
        query += "(("
        for field in range(len(search_fields)):
            if field < len(search_fields)-1:
                query += "({0}[{1}]) OR ".format(keyword, search_fields[field])
            else:
                query += "({0}[{1}])".format(keyword, search_fields[field])
        query += ") AND english[LANG])"

        handle = Entrez.esearch(db="pubmed", term=query, mindate=today.year-time_period, sort='Best Match')
        record = Entrez.read(handle)
        for record in record["IdList"]:
            if record not in search_results or "search_keywords" not in search_results[record]:
                search_results[record] = {"search_keywords": []}
            search_results[record]["search_keywords"].append(key)
    return search_results


def fetch_article(db_id):
    """
    Pesquisa artigos no pubmed pelo ID

    {
    "title":""
    "web_address":""
    "doi":""
    "abstract":""
    }

    :param db_id: ID
    :return: dicionário com título, doi, abstract e link do pubmed
    """
    document = {}
    handle = Entrez.efetch(db="pubmed", id=str(db_id), rettype="abstract", retmode="XML")
    record = Entrez.read(handle)
    article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
    document['title'] = article["ArticleTitle"]
    document['web_address'] = "https://pubmed.ncbi.nlm.nih.gov/{0}/".format(db_id)
    #TODO: melhorar sistema de procura de DOIs, porque estes podem nem sempre estar na posicao [2]
    #document['doi'] = record["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][2]
    if "Abstract" in article:
        document['abstract'] = article["Abstract"]["AbstractText"][0]
    else:
        document['abstract'] = None
    print(document)
    return document


def search_fetch_articles(search_term, search_keywords=["generic"], search_fields=['WORD', 'TIAB'], time_period=5):
    """
    Retorna um dicionário

    {
    bd_id:
        {
        "search_keywords": [],
        "title":""
        "web_address":""
        "doi":""
        "abstract":""
        }
    }

    :param search_term: termo
    :param search_keywords:
    :param search_fields:
    :param time_period:
    :return:
    """
    search_results = search_articles(search_term, search_keywords, search_fields, time_period)
    for article_id in search_results.keys():
        print(article_id)
        article_fetched = fetch_article(article_id)
        search_results[article_id]["title"] = article_fetched["title"]
        search_results[article_id]["web_address"] = article_fetched["web_address"]
        # search_results[article_id]["doi"] = article_fetched["doi"]
        search_results[article_id]["abstract"] = article_fetched["abstract"]
    print(search_results)
    return search_results


def search_print_articles(search_term, search_keywords=["generic"], search_fields=['WORD', 'TIAB'], time_period=5, file="search_results.md"):
    """
    Searches pubmed articles that might interest the reader for a certain topic, as well as small keyword variations.
    It then outputs them in a markdown file with metadata needed to find the article as well as its abstract
    :param db:
    :param search_term:
    :param search_keywords:
    :param search_fields:
    :param time_period:
    :param file:
    :return:
    """
    search_results = search_fetch_articles(search_term, search_keywords, search_fields, time_period)
    time_stamped_file = time_stamping(file)

    output = open(time_stamped_file, 'w')
    for search_result in search_results.keys():
        article = search_results[search_result]
        # title
        output.write("# {0}".format(article["title"])+"\n")

        # metadata
        for key in ["search_keywords", "web_address"]:
            output.write("{0}: {1}".format(key, article[key])+"\n")

        # abstract
        output.write("\n"+"## Abstract"+"\n")
        output.write(str(article["abstract"])+"\n"+"\n")
    output.close()
    return True
