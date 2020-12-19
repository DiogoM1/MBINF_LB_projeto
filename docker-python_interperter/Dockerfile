FROM python
# 3.7.9 fails the gplk
# https://stackoverflow.com/questions/62554991/how-do-i-install-python-on-alpine-linux

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
