'''
Análise da sequência e das features presentes no NCBI Deverá desenvolver scripts em BioPython que lhe permitam:
• aceder ao NCBI e guardar os ficheiros correspondentes aos genes escolhidos, podendo explorar possíveis variantes;
• verificar as anotações correspondentes aos genes de interesse;
• verificar e analisar a informação complementar fornecida pela lista de features e seus qualifiers; pode usar os campos de referências externas para identificar identificadores de outras bases de dados que permitam solidificar o conhecimento em relação a cada gene.
'''

############################### NCBI
import os
from Bio import Entrez
#from Bio import SeqIO

Entrez.email = "pedroalex123@gmail.com"


def get_lista_ids_do_gene(search_term):
    '''
    Procurar os IDs dos genes ORF7a, BST2 e ITGAL na base de dados nucleotide do NCBI.
    :param search_term:
    :return: todos os IDs das variantes dos genes
    '''
    handle = Entrez.esearch(db="nucleotide", term=str(search_term))
    record = Entrez.read(handle)
    return record["IdList"]


def nomesDosFicheiros(nome_gene, search_term):
    '''
    Cria o nome a ser utilizado na criação de cada ficheiro correspondente a cada id das variações de cada gene, na função escrever_genbank_nucleotide(id, nome_fich)
    :param nome_gene: lista dos nomes dos genes que se querem pesquisar
    :param search_term: lista com os organismos e os genes a pesquisar
    :return: dicionário com os genes e os seus respetivos IDs
    '''
    d = {}
    d[nome_gene] = get_lista_ids_do_gene(search_term)
    nome_ficheiro = []
    print("d=", d.items())
    for chave in d.keys():
        for valor in d.values():
            print("KVP", chave, valor)
    return nome_ficheiro


def escrever_genbank_nucleotide(id, nome_fich):
    '''
    Cria o ficheiro correspondente a cada id das variações de cada gene
    :param id:
    :param nome_fich:
    :return: ficheiros com nome de acordo com cada id do gene procurado, que contêm toda a informação existente na base de dados nucleotide em relação a esse id.
    '''
    handle = Entrez.efetch(db="nucleotide",
                           id=id,
                           rettype="gb", retmode="text")  # vai buscar à BD nucleotide os genes pretendidos
    ficheiroAescrever = os.path.join(os.getcwd(), nome_fich)  # junta a diretoria e o nome do ficheiro
    with open(ficheiroAescrever, 'w') as file:
        file.write(handle.read())


def escrever_fasta_nucleotide(id, nome_fich):
    '''
    Cria o ficheiro correspondente a cada id das variações de cada gene
    :param id:
    :param nome_fich:
    :return: ficheiros com nome de acordo com cada id do gene procurado, que contêm toda a informação existente na base de dados nucleotide em relação a esse id.
    '''
    handle = Entrez.efetch(db="nucleotide",
                           id=id,
                           rettype="fasta", retmode="text")
    ficheiroAescrever = os.path.join(os.getcwd(), nome_fich)
    with open(ficheiroAescrever, 'w') as file:
        file.write(handle.read())


def main():
    '''
    Interligação das funções anteriores (get_lista_ids_do_gene(search_term), nomesDosFicheiros(nome_gene, search_term), escrever_genbank_nucleotide(id, nome_fich)) com o objetivo de produzir ficheiros com informação correspondente a cada variação de cada gene (ORF7a, BST2, ITGAL).
    :return: ficheiros depositados na pasta data/resultados_GeneBank com o nome do gene e o ID de cada variente do gene
    '''
    nome_gene = ['ORF7a', 'BST2', 'ITGAL']
    genes = ['SARS Coronavirus[Orgn] AND ORF7a[Gene]',
             'Homo Sapiens[Orgn] AND BST2[Gene]',
             'Homo Sapiens[Orgn] AND ITGAL[Gene]']
    dict_nomes={}; dict_ficheiros={}
    for i in range(len(nome_gene)):
        lista_ids = get_lista_ids_do_gene(genes[i])
        dict_nomes.update({nome_gene[i]:lista_ids})

    #    #nome_ficheiro.append("{0}_{1}.gb".format(chave, valor))
    #print('ficheiros.gb')
    #os.chdir('..')
    #os.chdir('data/resultados_GeneBank')
    #for nome in dict_nomes.keys():
    #    lista_genes = dict_nomes.get(nome)
    #    for id in lista_genes:
    #        print(nome, id)
    #        escrever_genbank_nucleotide(id, "{0}_{1}.gb".format(nome, id))

main()


# TODO: query: dá-se lista e obtem-se resultados
# TODO: Créditos ao Afonso

