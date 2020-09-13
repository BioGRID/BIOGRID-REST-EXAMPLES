#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch interactions for use in a pandas dataframe
"""

import requests
import json
import pandas as pd
from core import config as cfg

request_url = cfg.BASE_URL + "/interactions"

# List of genes to search for
geneList = ["STE11", "NMD4"]  # Yeast Genes STE11 and NMD4
evidenceList = ["POSITIVE GENETIC", "PHENOTYPIC ENHANCEMENT"]

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json",  # Return results in TAB2 format
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

r = requests.get(request_url, params=params)
interactions = r.json()

# Create a hash of results by interaction identifier
data = {}
for interaction_id, interaction in interactions.items():
    data[interaction_id] = interaction
    # Add the interaction ID to the interaction record, so we can reference it easier
    data[interaction_id]["INTERACTION_ID"] = interaction_id

# Load the data into a pandas dataframe
dataset = pd.DataFrame.from_dict(data, orient="index")

# Re-order the columns and select only the columns we want to see

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
dataset = dataset[columns]

# Pretty print out the results
print(dataset)

""" 
Output as of version 4.0:
        INTERACTION_ID ENTREZ_GENE_A ENTREZ_GENE_B OFFICIAL_SYMBOL_A OFFICIAL_SYMBOL_B  EXPERIMENTAL_SYSTEM  PUBMED_ID       PUBMED_AUTHOR      THROUGHPUT          QUALIFICATIONS
80902            80902        855418        856382              CLA4             STE20  Synthetic Lethality   12686605  Goehring AS (2003)  Low Throughput                       -
80908            80908        855418        853350              CLA4              BCK1  Synthetic Lethality   12686605  Goehring AS (2003)  Low Throughput                       -
80909            80909        855418        852499              CLA4              BEM1  Synthetic Lethality   12686605  Goehring AS (2003)  Low Throughput                       -
80911            80911        855418        855942              CLA4              BEM4  Synthetic Lethality   12686605  Goehring AS (2003)  Low Throughput                       -
80912            80912        855418        855450              CLA4              BNI1  Synthetic Lethality   12686605  Goehring AS (2003)  Low Throughput                       -
...                ...           ...           ...               ...               ...                  ...        ...                 ...             ...                     ...
2757923        2757923        851029        850639              BUD6              SPA2                  PCA   31964708      Glomb O (2020)  Low Throughput         split-ubiquitin
2757929        2757929        855450        851029              BNI1              BUD6                  PCA   31964708      Glomb O (2020)  Low Throughput         split-ubiquitin
2757933        2757933        855450        853644              BNI1              CNB1                  PCA   31964708      Glomb O (2020)  Low Throughput         split-ubiquitin
2757934        2757934        855450        853133              BNI1              CRM1                  PCA   31964708      Glomb O (2020)  Low Throughput         split-ubiquitin
2766006        2766006        852754        855836              RPS2             HSP82   Proximity Label-MS   31689955    Schmitt K (2019)  Low Throughput  in the absence of Asc1
"""
