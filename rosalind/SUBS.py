#!/usr/bin/env python3

#Given: Two DNA strings s and t (each of length at most 1 kbp).
#Return: All locations of t as a substring of s.

# Plan:
# 1. find t sequence in s at each starting position
# 2. append index into list

from util import read_input

inp = "../rosalind_data/rosalind_subs.txt"
dna_proto = read_input(inp)

s = dna_proto[0]
t = dna_proto[1]

positions = []

for i in range(0, len(s)):
    if s.startswith(t, i): 
        positions.append(i+1)

print(*positions)