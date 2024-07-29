#!/usr/bin/env bash
# getOneKegg.sh
# Retrieve from KEGG API and append result to kegg.txt
curl https://rest.kegg.jp/conv/genes/uniprot:P12716 1>>kegg.txt 2>>kegg.errb
