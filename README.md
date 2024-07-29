# NGS Data Analysis and Transcriptome Assembly
* Organism Escherichia coli

## Purpose/Goal of the pipeline
* The pipeline has to create a reference genome database using the E.coli DNA-seq data.
* It collects and assembles E.coli RNA-seq data from scratch.
* At the end the genes are annotated and proteins translated by them are predicted.

## Required inputs
* SRR numbers of DNA-seq and RNA-seq data

## Required tools & resources (purpose explained in module steps) 
* fasterq-dump
* Trimmomatic
* SPAdes
* QUAST
* gmap_build
* Trinity
* hmmscan
* Transdecoder
* BLASTp

## Expected output
The following ar expected by the end of the pipeline:
* Reference genome database for E.coli
* Assembled transcriptome of E.coli
* Gene annotation and the predicted proteins


## Genome assembly from DNAseq data

* getNGS.sh: Get NGS data using fasterq-dump for Escherichia coli (DNA)
* trim.sh: Trim the sequences using the Trimmomatic
* runSpades.sh: Preliminary genome assembly of the DNA sequences using SPAdes
* runQuast.sh: Quality analysis of the assembly using QUAST. Get quality of the genome assembly, GC content and coverage.
* sbatch_assemble.sh: join all the scripts.

    ### Important tools used:
* fasterq-dump from SRA toolkit: Collects the sequence data from SRA, NCBI using the SRR number.
* Trimmomatic-0.39-2: A java based trimmer to remove parts of the sequence with low quality scores, and adapters.
* SPAdes v3.13.1: Genome assembler
* QUAST: Quality assessment tool.

    ### Requirements:
* Anaconda module must be loaded 
* source activate BINF-12-2021
* (Both done when the sbatch script is run. All the tools required for the steps were accessed here)

    ### Result:
* Stored all the scripts to scripts folder
* Got the DNA seq data, trimmed them and assembled using SPAdes.
* Assembly results stored in results/ecoli folder.
* Quast accessed data from results/ecoli/contigs.fasta and returned results to quast_results folder.
* Basic statistics of the preliminary assembly can be found in quast_results/latest/basic_stats

## Gene annotation
* EcoBuild: Extend the pipeline from last module by converting the Escherichia genome DNA seq into a reference for GSNAP.
* getNGS_RNAseq.sh: Get the RNA seq reads for Escherichia coli.

    ### Important tools used:
* gmap_build: creates a database from the DNA seqs, to be used for a reference-guided genome assembly.
* fasterq-dump: for the RNAseqs data

    ### Requirements:
* Anaconda module must be loaded 
* source activate BINF-12-2021
* (Both done when the sbatch script is run. All the tools required for the steps were accessed here)

    ### Results:
* Got 4 RNAseqs of Escherichia coli, and stored them in data/rawreads
* Used gmap_build to convert E.coli DNA seqs to a reference genome
* Stored the results in data/EcoliGmapDb folder

## Transcriptome assembly from RNAseq data
* trimAll.sh: Trims all the RNA sequences individually into paired and unpaired sequences.
* trinity_DeNovo.sh: Assembles all the RNA seq data de novo. Creates a fasta file called Trinity.fasta after the transcriptome assembly.  
* analyzeTrinity.sh: Checks the quality of the de novo assembly. Gives the N50 value to get an estimate about the quality. 
* sbatch_trinity.sh: Ties all the trinity scripts together into an sbatch script.

    ### Important tools used:
* Trimmomatic-0.39-2
* Trinity-v2.9.1 (available in the Anaconda module)
    
    ### Requirements:
* Anaconda module must be loaded 
* source activate BINF-12-2021
* (Both done when the sbatch script is run. All the tools required for the steps were accessed here)

    ### Results:
* Trimmed the RNAseqs and stored in data/trimmed/paired and data/trimmed/paired folders.
* Ran the Trinity sbatch script, and the Trinity.fasta file after the De Novo transcriptome assembly was stored in results/trinity_de_novo

    ### Additional steps taken:
* Failed Butterfly commands, Trinity ran for more than 10 hours and did not return a fasta output. 
* Re-ran the command manually, ran Trinity with --FORCE. Got the fasta results.

## Gene annotation and protein prediction
* longOrfs_args.sh: Find the longest open reading frames and translate them to protein sequences. 
* blastPep_args: aligns the long ORFs to SwissProt database to identify similar proteins to guide the protein prediction. 
* pfamScan_args: Uses HMM(Hidden Markov Model) to find protein domains.
* predictProteins_args: Takes the ORFs, BLAST output and the domains from hmmscan to predict the protein.
* alignPredicted_args.sh: BLASTs the predicted proteins to SwissProt database to check for similar proteins.
* sbatch_Transdecoder: Ties all the scripts together into an sbatch script.

    ### Important tools used:
* Transdecoder: Transdecoder.LongOrfs and Transdecoder.Predict.
* hmmscan
* BLASTp

    ### Requirements:
* Anaconda module must be loaded 
* source activate BINF-12-2021
* (Both done when the sbatch script is run. All the tools required for the steps were accessed here)


