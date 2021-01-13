from Bio.Blast import NCBIWWW, NCBIXML
import os

class BLASTer:
    def __init__(self, assession, fasta):
        self.assession = assession

    def blast(ID):
        result_handle = NCBIWWW.qblast("blastn", "nt", str(ID))
        txt = result_handle.read()
        print(txt)

    def blast_from_file(self):
        return



    """#parser e depois por ordem definição do melhor e score

    #record = SeqIO.read("m_cold.fasta", format="fasta")
    #result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    #with open("my_blast.xml", "w") as out_handle:
    #    out_handle.write(result_handle.read())
    #result_handle.close()
    #result_handle = open("my_blast.xml")"""


    """def find_homolg_files(ficheiro):
        '''
        Usar ficheiros existentes na nossa posse, encontrar homologos
        :param ficheiro:
        :return: homologos lindos
        '''
        fasta_string = open(str(ficheiro)).read()
        result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
        return result_handle"""


    """def function_from_homolg(gene):
        pass"""


    """def main():
        os.chdir('..')
        os.chdir('data/GeneBank')
        with open(r'GeneBank', 'rt') as fich: #Because "r" for read, and "t" for text are the default values, you do not need to specify them.
            for f in fich:
                # fich.read(f, 'rt')
                find_homolg(f)"""

        # ou ver https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

   """ def homolg_id(id, location = None):
        result_handle = NCBIWWW.qblast("blastn", "nt", id)
        for i in range(0,10):
            aln = result_handle.alignments[i]
            print(aln.title)"""


    #TODO: fazer blast e guardar ficheiro
    #TODO: filtrar o ID de todos os homologos
    #TODO: Correr
    # TODO: scores dos homologos e print por ordem?