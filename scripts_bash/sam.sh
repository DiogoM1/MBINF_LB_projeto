#! /bin/sh

REF="$1"
SEQ="$2"
WORKDIR="/opt/project/data/mutants"

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