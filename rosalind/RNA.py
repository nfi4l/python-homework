#!/usr/bin/env python3

#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

from util import import_file

inp = "../rosalind_data/rosalind_rna.txt"
dna = import_file(inp)

rna = ""

for letter in dna:
    if letter == "T":
        rna += "U"
    if letter == "A":
        rna += "A"
    if letter == "C":
        rna += "C"
    if letter == "G":
        rna += "G"
    
print(rna)
