#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch a single interaction using an interaction ID
"""

import requests
import json
from core import config as cfg

interaction_id = 439969
request_url = cfg.BASE_URL + "/interactions/" + str(interaction_id)

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
# In this particular instance, we've chosen to return results in json format
params = {"accesskey": cfg.ACCESS_KEY, "format": "json"}

r = requests.get(request_url, params=params)
interaction = r.json()

# Pretty print out the results
print(json.dumps(interaction, indent=4, sort_keys=True))

""" 
Output as of version 4.0:
{
    "439969": {
        "BIOGRID_ID_A": 33287,
        "BIOGRID_ID_B": 31905,
        "BIOGRID_INTERACTION_ID": 439969,
        "ENTREZ_GENE_A": "852931",
        "ENTREZ_GENE_B": "851396",
        "EXPERIMENTAL_SYSTEM": "Affinity Capture-MS",
        "EXPERIMENTAL_SYSTEM_TYPE": "physical",
        "MODIFICATION": "-",
        "OFFICIAL_SYMBOL_A": "KSS1",
        "OFFICIAL_SYMBOL_B": "STE7",
        "ONTOLOGY_TERMS": {},
        "ORGANISM_A": 559292,
        "ORGANISM_B": 559292,
        "PUBMED_AUTHOR": "Breitkreutz A (2010)",
        "PUBMED_ID": 20489023,
        "QUALIFICATIONS": "-",
        "QUANTITATION": "1.0",
        "SOURCEDB": "BIOGRID",
        "SYNONYMS_A": "mitogen-activated serine/threonine-protein kinase KSS1|L000000922",
        "SYNONYMS_B": "mitogen-activated protein kinase kinase STE7|L000002117",
        "SYSTEMATIC_NAME_A": "YGR040W",
        "SYSTEMATIC_NAME_B": "YDL159W",
        "TAGS": "-",
        "THROUGHPUT": "High Throughput"
    }
}
"""

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
# In this particular instance, we've chosen to return results in tab2 format with a header
params = {"accesskey": cfg.ACCESS_KEY, "format": "tab2", "includeHeader": "true"}

r = requests.get(request_url, params=params)
interaction = r.text

# Pretty print out the results
print(interaction)

""" 
Output as of version 4.0:
#BioGRID Interaction ID Entrez Gene Interactor A        Entrez Gene Interactor B        BioGRID ID Interactor A BioGRID ID Interactor B Systematic Name Interactor A    Systematic Name Interactor B    Official Symbol Interactor A       Official Symbol Interactor B    Synonyms Interactor A   Synonyms Interactor B   Experimental System     Experimental System Type        Author  Pubmed ID       Organism Interactor A   Organism Interactor B   ThroughputScore    Modification    Phenotypes      Qualifications  Tags    Source Database
439969  852931  851396  33287   31905   YGR040W YDL159W KSS1    STE7    mitogen-activated serine/threonine-protein kinase KSS1|L000000922       mitogen-activated protein kinase kinase STE7|L000002117 Affinity Capture-MS     physical   Breitkreutz A (2010)    20489023        559292  559292  High Throughput 1.0     -       -       -       -       BIOGRID
"""
