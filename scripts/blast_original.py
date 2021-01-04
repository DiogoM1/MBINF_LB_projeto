
'''
Análise de homologias por BLAST
As ferramentas de procura de homologias serão de especial relevo, nomeadamente para a procura de genes homólogos, bem como para a caracterização funcional dos genes selecionados.

    No primeiro caso, deverá configurar adequadamente as suas pesquisas ao nível da base de dados e desenvolver código para automatizar a decisão de existência de homologias significativas.

    No segundo caso, poderá analisar a lista de sequências homólogas e identificar padrões consistentes ao nível da função desempenhada por estas.

Deverá implementar scripts Python/ BioPython para automatizar estas tarefas.
'''

############################### BLAST


from Bio.Blast import NCBIWWW, NCBIXML
import os


def blaster(ID):
    result_handle = NCBIWWW.qblast("blastn", "nt", str(ID))
    txt = result_handle.read()
    print(txt)



#parser e depois por ordem definição do melhor e score

#record = SeqIO.read("m_cold.fasta", format="fasta")
#result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
#with open("my_blast.xml", "w") as out_handle:
#    out_handle.write(result_handle.read())
#result_handle.close()
#result_handle = open("my_blast.xml")


def find_homolg_files(ficheiro):
    '''
    Usar ficheiros existentes na nossa posse, encontrar homologos
    :param ficheiro:
    :return: homologos lindos
    '''
    fasta_string = open(str(ficheiro)).read()
    result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
    return result_handle


def function_from_homolg(gene):
    pass


def main():
    os.chdir('..')
    os.chdir('data/resultados_GeneBank')
    with open(r'resultados_GeneBank', 'rt') as fich: #Because "r" for read, and "t" for text are the default values, you do not need to specify them.
        for f in fich:
            # fich.read(f, 'rt')
            find_homolg(f)

    # ou ver https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder


# main()


# TODO: scores dos homologos e print por ordem?