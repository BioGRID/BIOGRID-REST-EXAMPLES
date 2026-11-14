#!/usr/bin/env python3

"""
Fetch interactions for use in a polars dataframe
"""

import polars as pl

from core import client
from core import config as cfg
from core.logger import logger

request_path = "/interactions"

# List of genes to search for
geneList = ["STE11", "NMD4"]  # Yeast Genes STE11 and NMD4
evidenceList = ["POSITIVE GENETIC", "PHENOTYPIC ENHANCEMENT"]

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json",  # Return results in JSON format
    "geneList": "|".join(geneList),  # Must be | separated
    "searchNames": "true",  # Search against official names
    "includeInteractors": "true",  # Set to true to get any interaction involving EITHER gene, set to false to get interactions between genes
    "includeInteractorInteractions": "true",  # Set to true to get interactions between the geneList’s first order interactors
    "taxId": 559292,  # Limit to Saccharomyces cerevisiae
    "evidenceList": "|".join(evidenceList),  # Exclude these two evidence types
    "includeEvidence": "false",  # If false "evidenceList" is evidence to exclude, if true "evidenceList" is evidence to show
}

# Additional options to try, you can uncomment them as necessary
# See "get_interactions_by_gene.py" or https://wiki.thebiogrid.org/doku.php/biogridrest for a list of additional parameter options

r = client.get(request_path, params=params)
interactions = r.json()

# Columns we want to see, in the order we want to see them
columns = [
    "INTERACTION_ID",
    "ENTREZ_GENE_A",
    "ENTREZ_GENE_B",
    "OFFICIAL_SYMBOL_A",
    "OFFICIAL_SYMBOL_B",
    "EXPERIMENTAL_SYSTEM",
    "PUBMED_ID",
    "PUBMED_AUTHOR",
    "THROUGHPUT",
    "QUALIFICATIONS",
]

# Build one row per interaction, adding the interaction ID (the key of the JSON object) to each record
rows = [{"INTERACTION_ID": interaction_id, **interaction} for interaction_id, interaction in interactions.items()]

# Load only the columns listed above into a polars dataframe, scanning every row to infer their types
dataset = pl.from_dicts(rows, schema=columns, infer_schema_length=None)
logger.debug("Loaded {} interactions into a polars dataframe", dataset.height)

# Log out the results, widening the table so every column is visible
with pl.Config(tbl_cols=-1, tbl_width_chars=250):
    logger.info("\n{}", dataset)

"""
Output as of November 2026:
shape: (6_359, 10)
┌────────────────┬───────────────┬───────────────┬───────────────────┬───────────────────┬─────────────────────────┬───────────┬─────────────────────────┬─────────────────┬─────────────────────────────────┐
│ INTERACTION_ID ┆ ENTREZ_GENE_A ┆ ENTREZ_GENE_B ┆ OFFICIAL_SYMBOL_A ┆ OFFICIAL_SYMBOL_B ┆ EXPERIMENTAL_SYSTEM     ┆ PUBMED_ID ┆ PUBMED_AUTHOR           ┆ THROUGHPUT      ┆ QUALIFICATIONS                  │
│ ---            ┆ ---           ┆ ---           ┆ ---               ┆ ---               ┆ ---                     ┆ ---       ┆ ---                     ┆ ---             ┆ ---                             │
│ str            ┆ str           ┆ str           ┆ str               ┆ str               ┆ str                     ┆ i64       ┆ str                     ┆ str             ┆ str                             │
╞════════════════╪═══════════════╪═══════════════╪═══════════════════╪═══════════════════╪═════════════════════════╪═══════════╪═════════════════════════╪═════════════════╪═════════════════════════════════╡
│ 76746          ┆ 851190        ┆ 853056        ┆ CDC24             ┆ RSR1              ┆ Dosage Rescue           ┆ 12960420  ┆ Kozminski KG (2003)     ┆ Low Throughput  ┆ -                               │
│ 80902          ┆ 855418        ┆ 856382        ┆ CLA4              ┆ STE20             ┆ Synthetic Lethality     ┆ 12686605  ┆ Goehring AS (2003)      ┆ Low Throughput  ┆ -                               │
│ 80908          ┆ 855418        ┆ 853350        ┆ CLA4              ┆ BCK1              ┆ Synthetic Lethality     ┆ 12686605  ┆ Goehring AS (2003)      ┆ Low Throughput  ┆ -                               │
│ 80909          ┆ 855418        ┆ 852499        ┆ CLA4              ┆ BEM1              ┆ Synthetic Lethality     ┆ 12686605  ┆ Goehring AS (2003)      ┆ Low Throughput  ┆ -                               │
│ 80911          ┆ 855418        ┆ 855942        ┆ CLA4              ┆ BEM4              ┆ Synthetic Lethality     ┆ 12686605  ┆ Goehring AS (2003)      ┆ Low Throughput  ┆ -                               │
│ …              ┆ …             ┆ …             ┆ …                 ┆ …                 ┆ …                       ┆ …         ┆ …                       ┆ …               ┆ …                               │
│ 3970393        ┆ 850647        ┆ 855418        ┆ PUF3              ┆ CLA4              ┆ Affinity Capture-MS     ┆ 42315289  ┆ Audebert L (2026)       ┆ High Throughput ┆ -                               │
│ 3970451        ┆ 850647        ┆ 856382        ┆ PUF3              ┆ STE20             ┆ Affinity Capture-MS     ┆ 42315289  ┆ Audebert L (2026)       ┆ High Throughput ┆ -                               │
│ 3970471        ┆ 856600        ┆ 855512        ┆ EGD2              ┆ SSB2              ┆ Synthetic Growth Defect ┆ 42538864  ┆ Bravo-Arevalo JE (2026) ┆ Low Throughput  ┆ EGD2/ EGD1/ BTT1/ SSB1/ SSB2 q… │
│ 3970474        ┆ 856600        ┆ 855512        ┆ EGD2              ┆ SSB2              ┆ Synthetic Rescue        ┆ 42538864  ┆ Bravo-Arevalo JE (2026) ┆ Low Throughput  ┆ EGD2/ EGD1/ BTT1/ SSB1/ SSB2 q… │
│ 3970477        ┆ 856600        ┆ 855512        ┆ EGD2              ┆ SSB2              ┆ Phenotypic Suppression  ┆ 42538864  ┆ Bravo-Arevalo JE (2026) ┆ Low Throughput  ┆ EGD2/ EGD1/ BTT1/ SSB1/ SSB2 q… │
└────────────────┴───────────────┴───────────────┴───────────────────┴───────────────────┴─────────────────────────┴───────────┴─────────────────────────┴─────────────────┴─────────────────────────────────┘
"""
