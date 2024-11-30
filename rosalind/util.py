# a library of utility functions for Rosalind exercises

#import rosalind input (first line)
def read_input(filepath):
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

#import entire file content
def import_file (filepath):
    with open(filepath, "r") as imp:
        imp_file = imp.read()
    return imp_file

#create complement dna strand
def complement(x):
    if x == "A":
        return "T"
    if x == "C":
        return "G"
    if x == "G":
        return "C"
    if x == "T":
        return "A"
    else:
        return "N"

def find_orfs(rna):
    stop_codons = ["UAA", "UAG", "UGA"]
    orfs=[]

    for i in range(len(rna)): #make index to look for codons and loop over rna
        if rna[i:i+3] == "AUG": #if rna codon equals start codon
            for j in range (i+3, len(rna), 3): #start at AUG and go in steps of 3 to find stop codons
                if rna[j:j+3] in stop_codons: #if codon equals stop codons
                    orfs.append(rna[i:j+3]) #input sequence from start to stop
                    break #and terminate loop
    return orfs

#protein code
code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}