#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch the set of currently supported experimental evidence types
"""

import requests
import json
from core import config as cfg

request_url = cfg.BASE_URL + "/evidence"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
# In this particular instance, we've chosen just the format to use in tab
params = {"accesskey": cfg.ACCESS_KEY, "format": "tab"}

r = requests.get(request_url, params=params)
evidence = r.text

# Pretty print out the results
print(evidence)

""" 
Expected Output as of version 4.0:
AFFINITY CAPTURE-LUMINESCENCE
AFFINITY CAPTURE-MS
AFFINITY CAPTURE-RNA
AFFINITY CAPTURE-WESTERN
BIOCHEMICAL ACTIVITY
CO-CRYSTAL STRUCTURE
CO-FRACTIONATION
CO-LOCALIZATION
CO-PURIFICATION
DOSAGE GROWTH DEFECT
DOSAGE LETHALITY
DOSAGE RESCUE
FAR WESTERN
FRET
NEGATIVE GENETIC
PCA
PHENOTYPIC ENHANCEMENT
PHENOTYPIC SUPPRESSION
POSITIVE GENETIC
PROTEIN-PEPTIDE
PROTEIN-RNA
PROXIMITY LABEL-MS
RECONSTITUTED COMPLEX
SYNTHETIC GROWTH DEFECT
SYNTHETIC HAPLOINSUFFICIENCY
SYNTHETIC LETHALITY
SYNTHETIC RESCUE
TWO-HYBRID
"""
