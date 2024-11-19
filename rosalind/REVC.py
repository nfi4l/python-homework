#!/usr/bin/env python3

#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

from util import import_file

inp = "../rosalind_data/rosalind_revc.txt"
dna = import_file(inp)

comp = ""
rev = ""

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
    
for base in dna:
    comp = comp + str(complement(base))

rev = comp[::-1]

print(rev)