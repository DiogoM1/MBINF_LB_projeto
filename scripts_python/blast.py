from Bio.Blast import NCBIWWW, NCBIXML
import os


class BLASTer:
    def __init__(self, accession="", fasta="", type="blastn", db="nt", e_thresh=0.05):
        self.accession = str(accession)
        self.fasta = fasta
        self.type = type
        self.db = db
        self.e_thresh = e_thresh

    def blast_from_accession(self):
        result_handle = NCBIWWW.qblast(self.type, self.db, self.accession)
        return result_handle

    def blast_from_file(self):
        result_handle = NCBIWWW.qblast(self.type, database=self.db, sequence=self.fasta.format("fasta"))
        return result_handle

    def blast_from_to_files(self):
        result_handle = self.blast_from_file()
        save_file = open("aula9_blast.xml", "w")
        save_file.write(result_handle.read())
        save_file.close()
        result_handle.close()

    #TODO: fazer blast e guardar ficheiro
    #TODO: filtrar o ID de todos os homologos
    #TODO: Correr
    # TODO: scores dos homologos e print por ordem?