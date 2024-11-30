#!/usr/bin/env python3

#Given: A DNA string s of length at most 1 kbp in FASTA format.
#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

#Plan:
# 1. dna -> transcribe to rna
# 2. dna -> reverse complement -> transcribe
# 3. create dictionary for proteins
# 4. find orfs(rna) ->return mRNA
# 5. translate into peptides using code dictionary

#======================================

from util import read_input

#import seq from fasta
inp = read_input("../rosalind_data/rosalind_orf.txt")
dna = ''.join(inp[1:])

print(dna)

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
    
# def find_orf (rna):
    
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

# transcribe forward DNA into RNA_f
rna_f=dna.replace("T","U")

#create reverse complement strand
comp = ""
rev = ""
    
for base in dna:
    comp = comp + (complement(base))

rev = comp[::-1]

#transcribe reverse DNA into RNA_r
rna_r=rev.replace("T","U")

#checkpoint
# print("rna strand:" + rna_f)
# print("~~~")
# print("reverse complementary strand:" + rev)
# print("~~~")
# print("reverse rna strand:" + rna_r)
# print("")

#find the orfs in RNA_f & RNA_r
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

mrna_f = find_orfs(rna_f)
mrna_r = find_orfs(rna_r)

#output mRNA_f & mRNA_r checkpoint
# print("mRNA forward:" + str(mrna_f))
# print("~~~")
# print("mRNA reverse:" + str(mrna_r))

#combine fwd & rev mrna
orfs = mrna_r+mrna_f

#translate mRNA_f & mRNA_r into prot
def translate(mrna):
    prot_str = ""
    for start in range(0, len(mrna), 3):
        codon = mrna[start:start+3]
        aminoacid = code[codon]
        if aminoacid == "Stop":
            continue
        prot_str += aminoacid
    return prot_str

#translate orfs
peptides = []
for orf in orfs: #translate each orf into proteins
    protein = translate(orf) 
    if protein not in peptides: #avoid duplicates -> if protein doesn't already exist, add
        peptides.append(protein)

print("")
print("ORFs:")
print("")

for protein in peptides:
    print(protein)