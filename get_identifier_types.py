#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch the set of currently supported identifier types
"""

import requests
import json
from core import config as cfg

request_url = cfg.BASE_URL + "/identifiers"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
# In this particular instance, we've chosen just the format to use in tab
params = {"accesskey": cfg.ACCESS_KEY, "format": "tab"}

r = requests.get(request_url, params=params)
identifiers = r.text

# Pretty print out the results
print(identifiers)

""" 
Expected Output as of version 4.0:
ANIMALQTLDB
APHIDBASE
BEEBASE
BGD
BIOGRID
CGD
CGNC
DICTYBASE
ECOGENE
ENSEMBL
ENSEMBL_GENE
ENSEMBL_PROTEIN
ENSEMBL_RNA
ENTREZ_GENE
ENTREZ_GENE_ETG
FLYBASE
GRID_LEGACY
HGNC
HPRD
IMGT/GENE-DB
MAIZEGDB
MGI
MIM
MIRBASE
OFFICIAL_SYMBOL
ORDERED_LOCUS
PBR
REFSEQ-LEGACY
REFSEQ-PROTEIN-ACCESSION
REFSEQ-PROTEIN-ACCESSION-VERSIONED
REFSEQ-PROTEIN-GI
REFSEQ-RNA-ACCESSION
REFSEQ-RNA-GI
RGD
SGD
SWISS-PROT
SYNONYM
SYSTEMATIC_NAME
TAIR
TREMBL
TUBERCULIST
UNIPROT-ACCESSION
UNIPROT-ISOFORM
UNIPROT_PRO
VECTORBASE
VEGA
WORMBASE
WORMBASE-OLD
XENBASE
ZFIN
"""
