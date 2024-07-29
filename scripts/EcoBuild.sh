#!/usr/bin/env bash
# EcoBuild.sh
# Usage: bash scripts/EcoBuild.sh 1>results/logs/EcoBuild.log 2>results/logs/EcoBuild.err &

gmap_build -D data \
-d EcoliGmapDb \
/scratch/paul.i/BINF6308/final_project_Escherichia/\
results/ecoli/contigs.fasta
