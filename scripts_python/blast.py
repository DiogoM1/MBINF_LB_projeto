# aqui caralho
'''
Análise de homologias por BLAST
As ferramentas de procura de homologias serão de especial relevo, nomeadamente para a procura de genes homólogos, bem como para a caracterização funcional dos genes selecionados.

    No primeiro caso, deverá configurar adequadamente as suas pesquisas ao nível da base de dados e desenvolver código para automatizar a decisão de existência de homologias significativas.

    No segundo caso, poderá analisar a lista de sequências homólogas e identificar padrões consistentes ao nível da função desempenhada por estas.

Deverá implementar scripts Python/ BioPython para automatizar estas tarefas.
'''

from Bio.Blast import NCBIWWW


def homolg_id(id, location = None):
    result_handle = NCBIWWW.qblast("blastn", "nt", id)
    for i in range(0,10):
        aln = result_handle.alignments[i]
        print(aln.title)


#TODO: fazer blast e guardar ficheiro
#TODO: filtrar o ID de todos os homologos
#TODO: Correr