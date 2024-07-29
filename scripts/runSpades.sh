#!/usr/bin/env bash
# runSpades.sh

mkdir -p "results/"
mkdir -p "results/ecoli/"

function Spades {
    spades.py \
    -1 data/SRR22746934_1.fastq \
    -2 data/SRR22746934_2.fastq \
    -o results/ecoli
}

Spades # runs the function Spades
