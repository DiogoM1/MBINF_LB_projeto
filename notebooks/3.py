'''
Análise da sequência e das features presentes no NCBI Deverá desenvolver scripts em BioPython que lhe permitam:
• aceder ao NCBI e guardar os ficheiros correspondentes aos genes escolhidos, podendo explorar possíveis variantes;
• verificar as anotações correspondentes aos genes de interesse;
• verificar e analisar a informação complementar fornecida pela lista de features e seus qualifiers; pode usar os campos de referências externas para identificar identificadores de outras bases de dados que permitam solidificar o conhecimento em relação a cada gene.
'''

# Procurar os IDs dos genes ORF7a, BST2 e ITGAL na base de dados nucleotide do NCBI.


from scripts.genebank import get_lista_ids_do_gene, escrever_genbank_nucleotide, escrever_genbank_nucleotide, nomesDosFicheiros
from scripts.blast import homolg_id

sarscov2_gene = ['ORF7a']
human_genes = ['BST2', 'ITGAL']

print("Sarscov 2")
print(get_lista_ids_do_gene("SARS Coronavirus", sarscov2_gene))
print("")
print("Human")
print(get_lista_ids_do_gene("Homo Sapiens", human_genes))

# Cria o ficheiro correspondente a cada id das variações de cada gene

"""escrever_genbank_nucleotide('1949110198', '/data/demo_genebank/')"""

homolg_id("1949110243")

"""
#nome_ficheiro.append("{0}_{1}.gb".format(chave, valor))
print('ficheiros.gb')
os.chdir('..')
os.chdir('data/resultados_GeneBank')
for nome in dict_nomes.keys():
    lista_genes = dict_nomes.get(nome)
    for id in lista_genes:
        print(nome, id)
        escrever_genbank_nucleotide(id, "{0}_{1}.gb".format(nome, id))
"""

# Fazer blast para os IDs dos genes virais e humanos de interesse

# Corona
"""
# Humano

print(homolg_id(get_lista_ids_do_gene("Homo Sapiens", human_genes)[0]))

"""