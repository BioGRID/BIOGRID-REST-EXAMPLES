#!/usr/bin/env python3

"""
Fetch the set of currently supported identifier types
"""

from core import client
from core import config as cfg
from core.logger import logger

request_path = "/identifiers"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
# In this particular instance, we've chosen just the format to use in tab
params = {"accesskey": cfg.ACCESS_KEY, "format": "tab"}

r = client.get(request_path, params=params)
identifiers = r.text

# Log out the results
logger.info("\n{}", identifiers)

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
