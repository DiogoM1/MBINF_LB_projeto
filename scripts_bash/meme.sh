#! /bin/sh

BLAST_RES="$1"
BLAST_RES_uni="$2"
REF="$3"
GENE="$4"
WORKDIR="/opt/project/data"

# meme "${WORKDIR}/${BLAST_RES_uni}" -protein -mod zoops -oc "${WORKDIR}/motif/${GENE}/meme" -nmotifs 5 -minw 6 -maxw 50

# fasta-get-markov "${BLAST_RES}" "${WORKDIR}/motif/${GENE}/markov"

# fimo --bfile --motif-- -oc "${WORKDIR}/motif/${GENE}/fimo" "${WORKDIR}/motif/${GENE}/meme/meme.txt" "${WORKDIR}/${REF}"

mast -bfile --motif-- -remcorr -oc "${WORKDIR}/motif/${GENE}/mast" "${WORKDIR}/motif/${GENE}/meme/meme.txt" "${WORKDIR}/${BLAST_RES}"