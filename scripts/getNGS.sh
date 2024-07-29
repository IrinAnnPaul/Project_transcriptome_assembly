#!/usr/bin/env bash
# getNGS.sh

# Retrieve the E.coli NGS reads.
mkdir -p data/
fasterq-dump --split-3 SRR22746934
