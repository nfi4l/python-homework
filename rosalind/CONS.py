#!/usr/bin/env python3

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

#Plan:
# 1. count bases of all sequences at each position -> create profile matrix
# 2. calculate which base occurs the most
# 3. create a consensus string from occurrences

from util import read_fasta

fasta = read_fasta('../rosalind_data/rosalind_cons.txt')

#print(fasta)

#extract sequences from fasta (without id)
seqs = []

for line in fasta.values():
        seqs.append(line)
        

# print(seqs)

# seqs = [
# "ATCCAGCT",
# "GGGCAACT",
# "ATGGATCT",
# "AAGCAACC",
# "TTGGAACT",
# "ATGCCATT",
# "ATGGCACT"
# ]

# create profile matrix of nucleotides from list of sequences
n = len(seqs[0]) #get seq length of first seq

#create matrix using position times length of seq
profile_matrix = {
    'A': [0] * n,
    'C': [0] * n, 
    'G': [0] * n,
    'T': [0] * n}

#count the bases
for dna in seqs:#loop over seqs
    for occurence, base in enumerate(dna):
        profile_matrix[base][occurence]+= 1

#print(profile_matrix)

#find consensus sequence

result = []

for i in range(n):
    max_count=0
    max_base=""
    for base in ["A", "C", "G", "T"]:
        count = profile_matrix[base][i]
        if count > max_count:#if count larger than max -> set to new max count and base
            max_count=count #set current count as max_count
            max_base=base #set current base as max_base
    result.append(max_base)#put max base into list

consensus = "".join(result)

print("consensus")
print(consensus)
