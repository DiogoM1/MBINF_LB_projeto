FROM python

# LABEL about the custom image
LABEL maintainer="diogodpmacedo@gmail.com"
LABEL version="0.1"
LABEL description="This is a small docker for the harmonization of bioinformatics tooling for the final LB project"

RUN apt update && \
    pip install --upgrade pip && \
# packages
    pip install biopython && \
    pip install PyVCF && \
    pip install bcbio-gff && \
    pip install jupyter
    # Neste momento o jupyter não está a funcionar, precisa de porta de saida e CMD para o correr assim que ligar, talvez criar um docker so para o "jupyter server"
