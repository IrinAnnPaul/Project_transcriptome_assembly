#!/usr/bin/env bash
# getNGS_RNAseq.sh

# Retrieve the Escherichia coli RNA seq reads.
fasterq-dump --split-3 SRR21849104 -O data/rawreads
fasterq-dump --split-3 SRR21849105 -O data/rawreads
fasterq-dump --split-3 SRR21849106 -O data/rawreads
fasterq-dump --split-3 SRR21849107 -O data/rawreads

mv data/rawreads/SRR21849104_1.fastq data/rawreads/Ecoli01.R1.fastq
mv data/rawreads/SRR21849104_2.fastq data/rawreads/Ecoli01.R2.fastq
mv data/rawreads/SRR21849105_1.fastq data/rawreads/Ecoli02.R1.fastq
mv data/rawreads/SRR21849105_2.fastq data/rawreads/Ecoli02.R2.fastq
mv data/rawreads/SRR21849106_1.fastq data/rawreads/Ecoli03.R1.fastq
mv data/rawreads/SRR21849106_2.fastq data/rawreads/Ecoli03.R2.fastq
mv data/rawreads/SRR21849107_1.fastq data/rawreads/Ecoli07.R1.fastq
mv data/rawreads/SRR21849107_2.fastq data/rawreads/Ecoli07.R2.fastq
