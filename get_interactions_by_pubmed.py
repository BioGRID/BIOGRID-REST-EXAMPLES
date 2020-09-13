#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch interactions for a specific set of publications
"""

import requests
import json
from core import config as cfg

request_url = cfg.BASE_URL + "/interactions"

# Two pubmed IDs to search for
pubmedList = ["20489023", "24142105"]  # Breitkreutz A (2010), Parua PK (2014)

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json",  # Return results in JSON format
    "pubmedList": "|".join(pubmedList),  # Must be | separated
    "excludePubmeds": "false",  # Set to true to EXCLUDE the pubmeds in the pubmedList
}

# Additional options to try, you can uncomment them as necessary
# See "get_interactions_by_gene.py" or https://wiki.thebiogrid.org/doku.php/biogridrest for a list of additional parameter options

r = requests.get(request_url, params=params)
interactions = r.json()

# Pretty print out the results
print(json.dumps(interactions, indent=4, sort_keys=True))

""" 
Output as of version 4.0:
{
    "1115074": {
        "BIOGRID_ID_A": 36930,
        "BIOGRID_ID_B": 32269,
        "BIOGRID_INTERACTION_ID": 1115074,
        "ENTREZ_GENE_A": "856924",
        "ENTREZ_GENE_B": "851802",
        "EXPERIMENTAL_SYSTEM": "Reconstituted Complex",
        "EXPERIMENTAL_SYSTEM_TYPE": "physical",
        "MODIFICATION": "-",
        "OFFICIAL_SYMBOL_A": "BMH1",
        "OFFICIAL_SYMBOL_B": "ADR1",
        "ONTOLOGY_TERMS": {},
        "ORGANISM_A": 559292,
        "ORGANISM_B": 559292,
        "PUBMED_AUTHOR": "Parua PK (2014)",
        "PUBMED_ID": 24142105,
        "QUALIFICATIONS": "Figure 1",
        "QUANTITATION": "-",
        "SOURCEDB": "BIOGRID",
        "SYNONYMS_A": "APR6|14-3-3 family protein BMH1|L000000185",
        "SYNONYMS_B": "DNA-binding transcription factor ADR1|L000000050",
        "SYSTEMATIC_NAME_A": "YER177W",
        "SYSTEMATIC_NAME_B": "YDR216W",
        "TAGS": "-",
        "THROUGHPUT": "Low Throughput"
    },
    "1115075": {
        "BIOGRID_ID_A": 36930,
        "BIOGRID_ID_B": 32078,
        "BIOGRID_INTERACTION_ID": 1115075,
        "ENTREZ_GENE_A": "856924",
        "ENTREZ_GENE_B": "851592",
        "EXPERIMENTAL_SYSTEM": "Reconstituted Complex",
        "EXPERIMENTAL_SYSTEM_TYPE": "physical",
        "MODIFICATION": "-",
        "OFFICIAL_SYMBOL_A": "BMH1",
        "OFFICIAL_SYMBOL_B": "REG1",
        "ONTOLOGY_TERMS": {},
        "ORGANISM_A": 559292,
        "ORGANISM_B": 559292,
        "PUBMED_AUTHOR": "Parua PK (2014)",
        "PUBMED_ID": 24142105,
        "QUALIFICATIONS": "Figure 4",
        "QUANTITATION": "-",
        "SOURCEDB": "BIOGRID",
        "SYNONYMS_A": "APR6|14-3-3 family protein BMH1|L000000185",
        "SYNONYMS_B": "HEX2|PZF240|SPP43|SRN1|protein phosphatase regulator REG1|L000001609",
        "SYSTEMATIC_NAME_A": "YER177W",
        "SYSTEMATIC_NAME_B": "YDR028C",
        "TAGS": "-",
        "THROUGHPUT": "Low Throughput"
    },
...
"441725": {
        "BIOGRID_ID_A": 35747,
        "BIOGRID_ID_B": 35200,
        "BIOGRID_INTERACTION_ID": 441725,
        "ENTREZ_GENE_A": "855648",
        "ENTREZ_GENE_B": "855043",
        "EXPERIMENTAL_SYSTEM": "Synthetic Rescue",
        "EXPERIMENTAL_SYSTEM_TYPE": "genetic",
        "MODIFICATION": "-",
        "OFFICIAL_SYMBOL_A": "MKS1",
        "OFFICIAL_SYMBOL_B": "TAP42",
        "ONTOLOGY_TERMS": {
            "92941": {
                "DESC": "The proportion of cells in a sample that are viable, i.e. able to form colonies. Often measured by spotting aliquots of a dilution series on a plate.",
                "FLAG": "P",
                "ID": 112,
                "NAME": "viability",
                "ONTOLOGY_CATEGORY": "phenotype",
                "ONTOLOGY_TERM_ID": "APO:0000111",
                "QUALIFIERS": {},
                "TYPE_ID": 4,
                "TYPE_NAME": "Unspecified"
            }
        },
        "ORGANISM_A": 559292,
        "ORGANISM_B": 559292,
        "PUBMED_AUTHOR": "Breitkreutz A (2010)",
        "PUBMED_ID": 20489023,
        "QUALIFICATIONS": "GAL-MKS1",
        "QUANTITATION": "-",
        "SOURCEDB": "BIOGRID",
        "SYNONYMS_A": "LYS80|L000001119",
        "SYNONYMS_B": "L000002599",
        "SYSTEMATIC_NAME_A": "YNL076W",
        "SYSTEMATIC_NAME_B": "YMR028W",
        "TAGS": "-",
        "THROUGHPUT": "Low Throughput"
    },
    "441727": {
        "BIOGRID_ID_A": 35747,
        "BIOGRID_ID_B": 33823,
        "BIOGRID_INTERACTION_ID": 441727,
        "ENTREZ_GENE_A": "855648",
        "ENTREZ_GENE_B": "853529",
        "EXPERIMENTAL_SYSTEM": "Synthetic Growth Defect",
        "EXPERIMENTAL_SYSTEM_TYPE": "genetic",
        "MODIFICATION": "-",
        "OFFICIAL_SYMBOL_A": "MKS1",
        "OFFICIAL_SYMBOL_B": "TOR1",
        "ONTOLOGY_TERMS": {
            "125708": {
                "DESC": "Growth under standard culture conditions (liquid or solid media).",
                "FLAG": "P",
                "ID": 107,
                "NAME": "vegetative growth",
                "ONTOLOGY_CATEGORY": "phenotype",
                "ONTOLOGY_TERM_ID": "APO:0000106",
                "QUALIFIERS": {},
                "TYPE_ID": 4,
                "TYPE_NAME": "Unspecified"
            }
        },
        "ORGANISM_A": 559292,
        "ORGANISM_B": 559292,
        "PUBMED_AUTHOR": "Breitkreutz A (2010)",
        "PUBMED_ID": 20489023,
        "QUALIFICATIONS": "GAL-MKS1",
        "QUANTITATION": "-",
        "SOURCEDB": "BIOGRID",
        "SYNONYMS_A": "LYS80|L000001119",
        "SYNONYMS_B": "DRR1|phosphatidylinositol kinase-related protein kinase TOR1|L000002322",
        "SYSTEMATIC_NAME_A": "YNL076W",
        "SYSTEMATIC_NAME_B": "YJR066W",
        "TAGS": "-",
        "THROUGHPUT": "Low Throughput"
    }
"""
