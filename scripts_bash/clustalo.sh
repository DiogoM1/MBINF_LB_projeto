#! /bin/sh

BLAST_RES="$1"
GENE="$2"
WORKDIR="/opt/project/data"
OUTPUT="${WORKDIR}/multi_align/${GENE}/${GENE}_"

clustalo -i "${WORKDIR}/${BLAST_RES}" -o "${WORKDIR}/multi_align/${GENE}/${GENE}_clustalo.fasta" --guidetree-out="${WORKDIR}/multi_align/${GENE}/${GENE}_clustalo.dnd" --outfmt=fa --force
# Não se pode exportar matrizes de distancias devido ao nº de seqs ser < 100
clustalo -i "${WORKDIR}/${BLAST_RES}" -o "${WORKDIR}/multi_align/${GENE}/${GENE}_clustalo.aln" --outfmt=clu --force
