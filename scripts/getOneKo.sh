#!/usr/bin/env bash
# getOneKo.sh

# Retrieve from KEGG API and append result to kegg.txt
curl https://rest.kegg.jp/link/ko/pon:100173097 1>ko.txt 2>ko.err
