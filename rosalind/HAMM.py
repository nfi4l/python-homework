#!/usr/bin/env python3

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

# Plan:
# 1. run both dna strings against each other
# 2. find mismatches
# 3. for mismatching nt add +1 to list

from util import read_input

inp = "../rosalind_data/rosalind_hamm.txt"
dna_proto = read_input(inp)

s = dna_proto[0]
t = dna_proto[1]

hamming_distance =[]

for nt in range(len(s)): #create nucleotide index from sequence length
# if nucleotide of s at index position is same as t, skip. if not, add 1 to list
    if s[nt] in t[nt]:
        continue
    else:
        hamming_distance.append(1)

# calculate hamming distance
print(sum(hamming_distance))