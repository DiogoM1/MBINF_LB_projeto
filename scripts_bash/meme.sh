#! /bin/sh

BLAST_RES="$1"
SEQ="$2"
WORKDIR="/opt/project/data/mottifs"

# Binarize aln
for ID in ${SEQ}
do
  FILE_NAME="${WORKDIR}/${ID}/${ID}"
  samtools view -Sb "${FILE_NAME}.aln.sam" > "${FILE_NAME}.aln.bam"
  samtools sort "${FILE_NAME}.aln.bam" -o "${FILE_NAME}.aln.sort.bam"
  samtools index "${FILE_NAME}.aln.sort.bam"
  samtools flagstat "${FILE_NAME}.aln.sort.bam" > "${FILE_NAME}_aln_stats"
done

# Verificar Alinhamentos

# TODO: is this needed ?
# samtools tview "${WORKDIR}/${ID}/${ID}.aln.sort.bam" "${REF}"


meme blast_results.fasta -mod oops

meme blast_results.fasta -mod oops
meme blast_results.fasta -mod zops
meme blast_results.fasta -mod zoops -o meme_zoops
meme blast_results.fasta -mod oops -o meme_oops
meme blast_results.fasta -mod oops -o meme_oops
meme blast_results.fasta -mod oops -oc meme_oops > meme_oops.txt
meme blast_results.fasta -mod zoops -oc meme_zoops > meme_zoops.txt
meme blast_results.fasta -mod anr -oc meme_anr > meme_anr.txt
meme blast_results.fasta -mod anr -oc meme_anr -nmotifs 20 > meme_anr.txt
meme blast_results.fasta -mod anr -oc meme_anr -nmotifs 20  > meme_anr.txt
meme blast_results.fasta -mod zoops -oc meme_zoops -nmotifs 20 > meme_zoops.txt
meme blast_results.fasta -mod oops -oc meme_oops -nmotifs 20 > meme_oops.txt
ls
exit
