from Bio import Entrez
from datetime import date, datetime

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

    {
    bd_id:
        {
        "search_keywords": [],
        }
    }

    :param search_keywords:
    :param search_term:
    :param time_period:
    :param search_fields: por título, autor, etc.
    :param db: base de dados a procurar
    :param term: termos a pesquisar
    :return: lista de IDs de artigos
    """
    today = date.today()
    search_results = {}

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

        for record in record["IdList"]:
            if record not in search_results or "search_keywords" not in search_results[record]:
                search_results[record] = {"search_keywords":[]}
            search_results[record]["search_keywords"] += key

    return search_results


def fetch_article(db_id, db="pubmed"):
    """
    Pesquisa artigos no pubmed pelo ID

    {
    "search_keywords": [],
    "title":""
    "web_address":""
    "doi":""
    "abstract":""
    }

    :param db_id: ID
    :param db: base de dados
    :return: dicionário com título, doi, abstract e link do pubmed
    """
    document = {}
    handle = Entrez.efetch(db=str(db), id=str(db_id), rettype="abstract", retmode="XML")
    record = Entrez.read(handle)
    article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
    document['title'] = article["ArticleTitle"]
    if db == "pubmed":
        document['web_address'] = "https://pubmed.ncbi.nlm.nih.gov/{0}/".format(db_id)
    document['doi'] = record["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][2]
    if "Abstract" in article:
        document['abstract'] = article["Abstract"]["AbstractText"][0]
    else:
        document['abstract'] = None
    return document


def search_fetch_articles(db, search_term, search_keywords=["generic"], search_fields=['WORD', 'TIAB'], time_period=5):
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

    :param db: base de dados
    :param search_term: termo
    :param search_keywords:
    :param search_fields:
    :param time_period:
    :return:
    """
    search_results = search_articles(db, search_term, search_keywords, search_fields, time_period)

    for article_id in search_results.keys():
        article_fetched = fetch_article(article_id, db)
        search_results[article_id]["title"] = article_fetched["title"]
        search_results[article_id]["web_address"] = article_fetched["web_address"]
        search_results[article_id]["doi"] = article_fetched["doi"]
        search_results[article_id]["abstract"] = article_fetched["abstract"]

    return search_results


def time_stamping(file):
    """
    Small function that datetime stamps file names and outputs
    :param file:
    :return:
    """
    time_stamp = datetime.now()

    # This method allows for the breaking appart of complex filenames like gene.vcf.tar.gz

    # 1st remove path like /home/
    # 2nd removes file formats
    # 3rd add time_stamp
    # 4th all is back together
    file_ = file.split(".", 1)
    file_[0] = str(file_[0]) + str(time_stamp)
    file = '.'.join(map(str, file_))
    return file


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
    search_results = search_fetch_articles("pubmed", search_term, search_keywords, search_fields, time_period)
    time_stamped_file = time_stamping(file)

    output = open(time_stamped_file, 'w')
    for search_result in search_results.keys():

        # title
        output.write("# {0}".format(search_result["title"])+"\n")

        # metadata
        for key in ["search_keywords" "web_address", "doi"]:
            output.write("{0}: {1}".format(key, search_result[key])+"\n")

        # abstract
        #
        output.write("\n""".format+"\n")
        output.write("\n")
    output.close()

