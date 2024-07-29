#!/usr/bin/env bash
# runQuast.sh

function Quast {
        quast.py results/ecoli/contigs.fasta
}

Quast
