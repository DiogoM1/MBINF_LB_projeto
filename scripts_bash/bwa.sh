#!/bin/bash

REF="$1"
SEQ="$2"
WORKDIR="/opt/project/data/mutants"

# Aln Procedures
bwa index "$REF"

for ID in ${SEQ}
do
  (
  for DIR in {1..2}
  do
    FILE_NAME="${WORKDIR}/${ID}/${ID}"
    bwa aln "${WORKDIR}/$REF" "${FILE_NAME}_${DIR}.fastq.gz" > "${FILE_NAME}_${DIR}.sai"
  done
  )
done &&

# shorter aln files than just one seq
echo "second part"
for ID in $SEQ
do
  FILE_NAME="${WORKDIR}/${ID}/${ID}"
  bwa sampe -f "${FILE_NAME}.aln.sam" "${WORKDIR}/${REF}" "${FILE_NAME}_1.sai" "${FILE_NAME}_2.sai" "${FILE_NAME}_1.fastq.gz" "${FILE_NAME}_2.fastq.gz"
done