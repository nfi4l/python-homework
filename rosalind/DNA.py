#!/usr/bin/env python3

#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def count_occurences(s):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for letter in s:
        if letter == "A":
            count_A += 1
        if letter == "C":
            count_C += 1
        if letter == "G":
            count_G += 1
        if letter == "T":
            count_T += 1
    return print(count_A, count_C, count_G, count_T)

#s: TTGTATTGGTTTACCGGCAAAAAGTCGTAAGAAACGCCCATTAGCGAGATCGCGAGTAGTAACCAGGCTCCTCCGATCTCGGGACTTCATGCAAAGAAGATGGTGCGAGGTCCAGGACTCGTATGCACGTAGTAGGACAAACCGATCCGTAATCCTCCAAACACGCTCCACATAATCTCCTTAGCACAATGCGTTTTAAGGAGCGAGCGAGGTCCAAGAAGGTATCACTTTGGCAGATTATTCTCCTAGTTCCTAACGTAGCACCAAGAACTGCAGCTCTCAGAACTAATCTAGCATGCCGCTTTGCTGTCTTTGTCGGGGACGTCTAAACGCTCTTGCATCTAGACTTACTAGCTCTGTGGTTCCAGAGCGGCAGCTAAGTGACTGTACACTGCTTTGCGCGGTGCACACCCCAGGTAAGACTAGATTACAGCCAGGACTGTTGAGAAACTTAGGGCCGCCCTCCAAAGCATCGCGGCCATGATGACAATCTGGGCTAGGAAGTTGACTTGTCAACCAGGCTGGGCTGCGCTCCCATGACTTGCGCACGCGATTCATGATTGAATACGGTACCACAGACCGCTAGTTTTAGGTCCTGGCATTTTTGCAGACAGCCCGAAGCAAAGCCCACCATTCGACGTCTTGGGCGGGCCGGGAGTGACCACATGTTCCCGCGTCATAACGGGCACGCTATAGCGTAGCCCTGGTGTTTGTGTAATGGTGACGCAGTATTGACACTCGTCGGCTGTAGCCGGTAAATGCCACGAGGGGGTACACAAGCACCTGCTAATTCAATTTACTGGGGATTGGGCTAAGGAATCTCTTGTAGAGGGAACCGCCAGGGATTCCTAGGAATCTGGTGACCTGTGAACGATGTTGAACAGTG
#Solution: 219 224 235 208