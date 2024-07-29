#!/bin/bash
#BATCH --partition=short               # choose from debug, express, or short
#SBATCH --job-name=assembleGenome
#SBATCH --time=04:00:00                 # the code pieces should run in far less than 4 hours
#SBATCH -N 1                            # nodes requested
#SBATCH -n 1                            # task per node requested
#SBATCH --output="batch-%x-%j.output"   # where to direct standard output; will be batch-jobname-jobID.output

echo "Starting our analysis $(date)"

ORGANISM="Ecoli"
SRR_ID=SRR22746934

echo "$ORGANISM SRR reads to process: $SRR_ID"

echo "Loading our BINF6308 Anaconda environment."
module load anaconda3/2021.11
source activate BINF-12-2021

echo "Downloading $SRR_ID reads $(date)"
bash /scratch/paul.i/BINF6308/final_project_Escherichia/scripts/getNGS.sh

echo "Trimming $SRR_ID reads $(date)"
bash /scratch/paul.i/BINF6308/final_project_Escherichia/scripts/trim.sh

echo "Assembling genome from trimmed $SRR_ID reads $(date)"
bash /scratch/paul.i/BINF6308/final_project_Escherichia/scripts/runSpades.sh

echo "Analyzing genome assembly $(date)"
bash /scratch/paul.i/BINF6308/final_project_Escherichia/scripts/runQuast.sh

echo "Assembly and analysis complete $(date)"
