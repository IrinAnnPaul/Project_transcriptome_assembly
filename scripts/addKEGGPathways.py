#!/usr/bin/env python
"""
This program uses sequential API calls to access KEGG and GO databases
to understand the functional and biological roles of protein sequences,
given a FASTA output file from protein BLAST.
"""

import argparse
import requests


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Using sequential APIs to access controlled vocabularies",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # argument for input file
    parser.add_argument('-i', '--infile',  # use args.infile to get this user input
                        metavar='infile',  # shorthand to represent the input value
                        help='Input file with BLAST output',
                        type=str,  # type of input expected
                        default='alignPredicted.txt',
                        required=True
                        )

    # argument for evalue threshold value
    parser.add_argument('-e', '--evalue',  # use args.evalue to get this user input
                        metavar='evalue',
                        help='E-value threshold of the BLAST output',
                        type=float,
                        default=1e-50,
                        required=True
                        )

    # argument for the output filename
    parser.add_argument('-o', '--outfile',
                        metavar='outfile',
                        help='Output filename',
                        type=str,
                        required=True
                        )

    return parser.parse_args()


def getUniProtFromBlast(blast_line, threshold):
    """Return UniProt ID from the BLAST line if the evalue is below the threshold.
    Returns False if e-value is above threshold.
    """
    cleaned_line = blast_line.strip()
    blast_fields = cleaned_line.split("\t")
    if float(blast_fields[7]) < float(threshold):
        return blast_fields[1]
    else:
        return False


def getKeggGene(uniprotID):
    """Return a list of KEGG organism:gene pairs for a provided UniProtID."""
    keggGenes = []
    result = requests.get(f'https://rest.kegg.jp/conv/genes/uniprot:{uniprotID}')
    try:
        for entry in result.iter_lines():
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggGenes.append(fields[1])  # second field is the keggGene value
    except IndexError:
        return False

    return keggGenes


def getKeggOrthology(keggID):
    """Return the KEGG orthology id for a provided KEGG ID"""
    kegg_ortho_id = []
    result_ln = requests.get(f"https://rest.kegg.jp/link/ko/{''.join(keggID)}")
    try:
        for entry in result_ln.iter_lines():
            str_entry = entry.decode(result_ln.encoding)
            fields = str_entry.split("\t")
            kegg_ortho_id.append(fields[1])
    except IndexError:
        return False

    return kegg_ortho_id


def getKeggPathIDs(koID):
    """Return a list of KEGG Path IDs for a provided KEGG Orthology ID"""
    kegg_path_id = []
    result = requests.get(f"https://rest.kegg.jp/link/pathway/{''.join(koID)}")
    try:
        for entry in result.iter_lines():
            str_entry = entry.decode(result.encoding)
            fields = str_entry.split("\t")
            kegg_path_id.append(fields[1])
    except IndexError:
        return False

    return kegg_path_id


def loadKeggPathways():
    """Return dictionary of key=pathID,
    value=pathway name from http://rest.kegg.jp/list/pathway/ko
    Example: keggPathways["path:ko00564"] = "Glycerophospholipid metabolism"
    """
    keggPathways = {}
    # only loads paths that start with 'path:ko'
    result = requests.get('https://rest.kegg.jp/list/pathway/ko')
    for entry in result.iter_lines():
        str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
        fields = str_entry.split("\t")
        keggPathways[fields[0]] = fields[1]

    return keggPathways


def addKEGGPathways(blast_file, threshold, f_out):
    """Ties all the functions together"""
    final_list = []
    for line in blast_file.readlines():
        uniprot_id = getUniProtFromBlast(line, threshold)
        if uniprot_id:
            kegg_id = getKeggGene(uniprot_id)
            if kegg_id:
                kegg_ortho = getKeggOrthology(kegg_id)
                if kegg_ortho:
                    kegg_path = getKeggPathIDs(kegg_ortho)
                    path_dict = loadKeggPathways()
                    if kegg_path:
                        for item in kegg_path:
                            if item in path_dict.keys():
                                final_list.append(line.strip())
                                final_list.append(''.join(kegg_ortho))
                                final_list.append(item)
                                final_list.append(path_dict[item])
                                output = "\t".join(str(item) for item in final_list)
                                f_out.write(output + "\n")

    return out_file


if __name__ == "__main__":
    args = get_args()
    infile = args.infile
    evalue = args.evalue
    out_file = args.outfile
    fh_i = open(infile, 'r')
    fh_o = open(out_file, 'w')
    output = addKEGGPathways(fh_i, evalue, fh_o)
    fh_i.close()
    fh_o.close()
