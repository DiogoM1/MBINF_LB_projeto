#! /bin/sh

REF="$1"
SEQ="$2"
WORKDIR="/opt/project/data/mutants"

#Identificar  os  variantes  eextrair para um ficheiro vcf
for ID in ${SEQ}
do
  FILE_NAME="${WORKDIR}/${ID}/${ID}"
  bcftools mpileup -Ou -f "${WORKDIR}/${REF}" "${FILE_NAME}.aln.sort.bam" | bcftools call -Ov -vc > "${FILE_NAME}.sars_cov.raw.vcf"
done