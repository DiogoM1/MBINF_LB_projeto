

############################### NCBI
import os
from Bio import Entrez
from pathlib import Path
from scripts_python.general import time_stamping
Entrez.email = "pedroalex123@gmail.com"


class gbSearch:
    '''
    Análise da sequência e das features presentes no NCBI Deverá desenvolver scripts em BioPython que lhe permitam:
    • aceder ao NCBI e guardar os ficheiros correspondentes aos genes escolhidos, podendo explorar possíveis variantes;
    • verificar as anotações correspondentes aos genes de interesse;
    • verificar e analisar a informação complementar fornecida pela lista de features e seus qualifiers; pode usar os campos de referências externas para identificar identificadores de outras bases de dados que permitam solidificar o conhecimento em relação a cada gene.
    '''
    def __init__(self, organism, genes, base_dir=os.getcwd(), database='nucleotide'):
        self.organism = organism
        self.genes = genes
        self.base_dir = base_dir
        self.database = database

    def get_ids(self, gene):
        '''
        Procurar os IDs dos genes ORF7a, BST2 e ITGAL na base de dados nucleotide do NCBI.
        :param gene:
        :return: todos os IDs das variantes dos genes
        '''
        search_term = "{0}[Orgn] AND {1}[Gene] AND {1}[Title]".format(self.organism, gene)
        handle = Entrez.esearch(db="nucleotide", term=str(search_term))
        record = Entrez.read(handle)
        return record["IdList"]

    def get_genes_ids(self):
        '''
        Procurar os IDs dos genes ORF7a, BST2 e ITGAL na base de dados nucleotide do NCBI.
        :return: todos os IDs das variantes dos genes
        '''
        results = {}
        for gene in self.genes:
            results[gene] = self.get_ids(gene)
        return results

    def write_file(self, gene, gene_id, file_type="gb"):
        '''
        Pesquisa um nucleótido no genbank com base no seu ID e retorna o resultado na forma de um ficheiro
        :param gene_id:
        :return: ficheiros com nome de acordo com cada id do gene procurado, que contêm toda a informação existente na base de dados nucleotide em relação a esse id.
        '''
        if file_type in ["gb", "fasta"] and self.database in ["nucleotide", "gene"]:
            handle = Entrez.efetch(db=self.database,
                                   id=gene_id,
                                   rettype=file_type,
                                   retmode="text")  # vai buscar à BD nucleotide os genes pretendidos
            file_dir = os.path.join(self.base_dir,"{0}-{1}".format(self.organism, gene))# junta a diretoria e o nome do ficheiro
            file_dir_time = time_stamping(file_dir)
            print(file_dir_time)
            file_name = "{0}_{1}.{2}".format(gene, gene_id, file_type)
            file_path = os.path.join(file_dir_time,file_name)
            Path(file_dir_time).mkdir(parents=True, exist_ok=True)

            with open(file_path, 'w') as file:
                file.write(handle.read())

    def get_files(self, file_type="gb"):
        '''
        Interligação das funções anteriores (get_lista_ids_do_gene(search_term), nomesDosFicheiros(nome_gene, search_term), escrever_genbank_nucleotide(id, nome_fich)) com o objetivo de produzir ficheiros com informação correspondente a cada variação de cada gene (ORF7a, BST2, ITGAL).
        :return: ficheiros depositados na pasta data/GeneBank com o nome do gene e o ID de cada variente do gene
        '''
        ids = self.get_genes_ids()

        for gene in ids.keys():
            ids_list = ids.get(gene)
            for gene_id in ids_list:
                self.write_file(gene, gene_id, file_type)

    def get_gb(self):
        return self.get_files("gb")

    def get_fasta(self):
        return self.get_files("fasta")