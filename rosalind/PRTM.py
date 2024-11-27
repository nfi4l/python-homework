#!/usr/bin/env python

# a script that will take an aminoacid sequence as input and print out
# the molecular weight of the peptide

# Instructions:
# 1. read the data
# 2. define the dictionary (key: amino acid one letter code, value: mass in Da)
# 3. (actual solution):
#   - define a counter variable, total_weight, and set it to 0
#   - loop over the input,
#   - for the current amino acid, take the value from the dictionary, and add it to total_weight
from util import read_input

inp = "../rosalind_data/rosalind_prtm.txt"
dna_proto = read_input(inp)

p = dna_proto[0]

total_weight = []

prot_weight = {
"A":   71.03711,
"C":   103.00919,
"D":   115.02694,
"E":   129.04259,
"F":   147.06841,
"G":   57.02146,
"H":   137.05891,
"I":   113.08406,
"K":   128.09496,
"L":   113.08406,
"M":   131.04049,
"N":   114.04293,
"P":   97.05276,
"Q":   128.05858,
"R":   156.10111,
"S":   87.03203,
"T":   101.04768,
"V":   99.06841,
"W":   186.07931,
"Y":   163.06333 
}

for id, weight in prot_weight.items(): #loop over dictionary items
    for x in range(len(p)): #create index
        if p[x] == id: #loop over index and compare to id
            total_weight.append(weight) #add to total_weight if keys are identical

print(sum(total_weight))