#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch interactions for a specific gene or gene list
"""

import requests
import json
from core import config as cfg

request_url = cfg.BASE_URL + "/interactions"

# List of genes to search for
geneList = ["STE11", "NMD4"]  # Yeast Genes STE11 and NMD4
evidenceList = ["POSITIVE GENETIC", "PHENOTYPIC ENHANCEMENT"]

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "tab2",  # Return results in TAB2 format
    "geneList": "|".join(geneList),  # Must be | separated
    "searchNames": "true",  # Search against official names
    "includeInteractors": "true",  # Set to true to get any interaction involving EITHER gene, set to false to get interactions between genes
    "taxId": 559292,  # Limit to Saccharomyces cerevisiae
    "evidenceList": "|".join(evidenceList),  # Exclude these two evidence types
    "includeEvidence": "false",  # If false "evidenceList" is evidence to exclude, if true "evidenceList" is evidence to show
    "includeHeader": "true",
}

# Additional options to try, you can uncomment them as necessary
# params["start"] = 5 # Specify where to start fetching results from if > 10,000 results being returned
# params["max"] = 10 # Specify the number of results to return, max is 10,000
# params["interSpeciesExcluded"] = "false" # true or false, If ‘true’, interactions with interactors from different species will be excluded (ex. no Human -> Mouse interactions)
# params["selfInteractionsExcluded"] = "false" # true or false, If ‘true’, interactions with one interactor will be excluded. (ex. no STE11 -> STE11 interactions)
# params["searchIds"] = "false" # true or false, If ‘true’, ENTREZ_GENE, ORDERED LOCUS and SYSTEMATIC_NAME (orf) will be examined for a match with the geneList
# params["searchSynonyms"] = "false" # true or false, If ‘true’, SYNONYMS will be examined for a match with the geneList
# params["searchBiogridIds"] = "false" # true or false, If ‘true’, BIOGRID INTERNAL IDS will be examined for a match with the geneList
# params["excludeGenes"] = "false" # true or false, If 'true' the geneList becomes a list of genes to EXCLUDE rather than to INCLUDE
# params["includeInteractorInteractions"] = "true" # true or false, If ‘true’ interactions between the geneList’s first order interactors will be included. Ignored if includeInteractors is ‘false’ or if excludeGenes is set to ‘true’.
# params["htpThreshold"] = 50 # Any publication with more than this many interactions will be excluded
# params["throughputTag"] = "any" # any, low, high. If set to low, only `low throughput` interactions will be returned, if set to high, only `high throughput` interactions will be returned
# params["additionalIdentifierTypes"] = "SGD|FLYBASE|REFSEQ" # You can specify a | separated list of additional identifier types to search against (see get_identifier_types.py)

r = requests.get(request_url, params=params)
interactions = r.text

# Pretty print out the results
print(interactions)

""" 
Output as of version 4.0:
#BioGRID Interaction ID Entrez Gene Interactor A        Entrez Gene Interactor B        BioGRID ID Interactor A BioGRID ID Interactor B Systematic Name Interactor A    Systematic Name Interactor B    Official Symbol Interactor A       Official Symbol Interactor B    Synonyms Interactor A   Synonyms Interactor B   Experimental System     Experimental System Type        Author  Pubmed ID       Organism Interactor A   Organism Interactor B   ThroughputScore    Modification    Phenotypes      Qualifications  Tags    Source Database
102009  856876  851076  36882   31623   YER136W YLR362W GDI1    STE11   SEC19|L000000699        mitogen-activated protein kinase kinase kinase STE11|L000002118 Affinity Capture-MS     physical        Ho Y (2002)     11805837  559292   559292  High Throughput -       -       -       -       -       BIOGRID
102073  852931  851076  33287   31623   YGR040W YLR362W KSS1    STE11   mitogen-activated serine/threonine-protein kinase KSS1|L000000922       mitogen-activated protein kinase kinase kinase STE11|L000002118 Affinity Capture-MSphysical        Ho Y (2002)     11805837        559292  559292  High Throughput -       -       -       -       -       BIOGRID
103805  854256  851076  34487   31623   YOR089C YLR362W VPS21   STE11   VPS12|VPT12|YPT21|YPT51|Rab family GTPase VPS21|L000002474      mitogen-activated protein kinase kinase kinase STE11|L000002118 Affinity Capture-MS     physical   Ho Y (2002)     11805837        559292  559292  High Throughput -       -       -       -       -       BIOGRID
113767  851076  850325  31623   30951   YLR362W YCL032W STE11   STE50   mitogen-activated protein kinase kinase kinase STE11|L000002118 L000002125      Two-hybrid      physical        Uetz P (2000)   10688190        559292  559292     High Throughput -       -       -       -       -       BIOGRID
136351  851680  851076  32160   31623   YDR103W YLR362W STE5    STE11   HMD3|NUL3|L000002115    mitogen-activated protein kinase kinase kinase STE11|L000002118 Affinity Capture-MS     physical        Feng Y (1998)   9501067 559292     559292  Low Throughput  -       -       -       -       -       BIOGRID
...
2515486 851077  855897  31624   35980   YLR363C YPL204W NMD4    HRR25   L000002938      KTI14|serine/threonine protein kinase HRR25|L000000810  Affinity Capture-MS     physical        Dehecq M (2018) 30275269        559292  559292     Low Throughput  -       -       -       -       -       BIOGRID
2515487 851077  854016  31624   34268   YLR363C YOL149W NMD4    DCP1    L000002938      MRT2|L000002960|L000003045|S000029311   Affinity Capture-MS     physical        Dehecq M (2018) 30275269        559292  559292  Low Throughput     -       -       -       -       -       BIOGRID
2515488 851077  856700  31624   36716   YLR363C YEL015W NMD4    EDC3    L000002938      DCP3|LSM16      Affinity Capture-MS     physical        Dehecq M (2018) 30275269        559292  559292  Low Throughput  -       -       - --       BIOGRID
2515489 851077  851787  31624   32256   YLR363C YDR206W NMD4    EBS1    L000002938      L000004629      Affinity Capture-MS     physical        Dehecq M (2018) 30275269        559292  559292  Low Throughput  -       -       - --       BIOGRID
2515490 851077  855104  31624   35256   YLR363C YMR080C NMD4    NAM7    L000002938      IFS2|MOF4|SUP113|UPF1|ATP-dependent RNA helicase NAM7|L000002429|S000029550|L000002232  Affinity Capture-MS     physical        Dehecq M (2018)    30275269        559292  559292  Low Throughput  -       -       -       -       -       BIOGRID
2535071 853537  851076  33830   31623   YJR074W YLR362W MOG1    STE11   L000004615      mitogen-activated protein kinase kinase kinase STE11|L000002118 Affinity Capture-MS     physical        Oliete-Calvo P (2018)   30249596  559292   559292  High Throughput -       -       -       -       -       BIOGRID
2561661 856303  851076  36346   31623   YPR173C YLR362W VPS4    STE11   CSC1|DID6|END13|GRD13|VPL4|VPT10|AAA family ATPase VPS4|L000002956      mitogen-activated protein kinase kinase kinase STE11|L000002118 Synthetic Growth Defect    genetic Schmidt O (2019)        31133554        559292  559292  Low Throughput  -       -       vegetative growth       -       -       BIOGRID
2595386 856303  851076  36346   31623   YPR173C YLR362W VPS4    STE11   CSC1|DID6|END13|GRD13|VPL4|VPT10|AAA family ATPase VPS4|L000002956      mitogen-activated protein kinase kinase kinase STE11|L000002118 Synthetic Lethalitygenetic Schmidt O (2019)        31368600        559292  559292  High Throughput -       -       inviable        SGA     -       BIOGRID
"""
