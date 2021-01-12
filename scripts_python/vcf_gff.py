from collections import defaultdict

import vcf
from BCBio import GFF


def vcf2dict(loc):
    """
    For a vcf file returns dict with all its records.

    The Key:Value pair is structured as {'position':'full vcf record object'}
    :param loc:string
    :return:dict{int:obj}
    """
    reader = vcf.Reader(open(loc, 'r'))
    records = {}
    for record in reader:
        records[record.POS] = record
    return records


def vcf_isec(vcf1, vcf2):
    """
    For 2 vcf dicts structured as {'position':'full vcf record object'}, returns the intersection of variants in a similarly structured dict.
    :param vcf1: dict{int:obj}
    :param vcf2: dict{int:obj}
    :return: dict{int:obj}
    """
    isec_records = {}
    for record in vcf1.keys():
        # https://stackoverflow.com/questions/3733992/determine-whether-a-key-is-present-in-a-dictionary
        if record in vcf2:
            isec_records[record] = vcf2[record]
    # Logic could be added to check if dict is empty or not as in:
    # https://stackoverflow.com/questions/23177439/python-checking-if-a-dictionary-is-empty-doesnt-seem-to-work
    # But for modularity this list will just return and empty dict
    return isec_records


def gff2rec(in_file):
    """
    For a gff or gtf file returns list with all its genes.
    :param in_file:string
    :return:list[object]
    """
    in_handle = open(in_file)
    # https://biopython.org/wiki/GFF_Parsing
    # This method is not good for massive gff files, read the doc
    records = []
    for record in GFF.parse(in_handle):
        # This is dirty Python
        records.append(record)
    in_handle.close()
    return records


def seq_rec_sgenes(record):
    """
    For SeqRecord returns list with all its genes that might have been studied for function.
    :param record:string
    :return:list[object]
    """
    studied_genes = []
    for feature in record.features:
        if feature.type == "gene" and feature.qualifiers['gene_name'] and feature.qualifiers['gene_biotype']:
            studied_genes.append(feature)
    return studied_genes


def lookup_var2genes(variations, gene):
    """
    For a SeqFeature objects, it performs a lookup of variations provided in a dict structured as {'position':'pyvcf record object'}.

    This operation returns a dict where for gene there is a list of variation positions.
    :param variations: dict{int:obj}
    :param record: list[object]
    :return: dict{string:list[int]}
    """
    # TODO: Perguntar ao stor os critérios de comparação
    genes_var = defaultdict(list)

    # The "gene_id" qualifier is a list of len 1 so I have to call the index 0 otherwise in futher opperations I will try to add a list as a dict key.
    # This raises an error as list are not hashable
    gene_id = gene.qualifiers['gene_id'][0]
    genes_var[gene_id] = []
    for var in variations.keys():
        # Variant position
        # Gene location using the logic in:
        # https://biopython.readthedocs.io/en/latest/api/Bio.SeqFeature.html#Bio.SeqFeature.FeatureLocation
        if gene.location.start <= variations[var].POS <= gene.location.end:
            # If the var is within the start and end of the gene, it means it belongs to it
            # how to add to lists inside dict:
            # https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary
            genes_var[gene_id].append(var)
    return genes_var
