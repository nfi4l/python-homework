#!/usr/bin/env python3

#Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#Return: The adjacency list corresponding to O3. You may return edges in any order.

from util import read_fasta

fasta = read_fasta('../rosalind_data/rosalind_grph.txt')
#print(fasta)

#==========================

#get the suffix of k
def k_suffix (seq, k):
    return seq[-k:]

#get the prefix of k
def k_prefix (seq, k):
    return seq[:k]

# testseq = "TTGCTTAAAATAATCTAGTTGAGGTCGCTATGGGGGATAAACGCCGAAGCGTTAAATGGCGTTCAATTGGAGTTGTCCAGGGAACGGCACAACTGATGGA"
# print(k_prefix(testseq, 3))
# print(k_suffix(testseq, 3))

#find overlaps(k) between sequences

def overlaps(fasta, k):
    overlaps = []
    #get sequence IDs
    ID = list(fasta.keys())
    #compare pairs
    for s_ID in ID: #substring s
        s_suffix = k_suffix(fasta[s_ID], k) #get suffix of s
        for t_ID in ID: #substring t
            if s_ID != t_ID: #s =/= t checkpoint
                t_prefix = k_prefix(fasta[t_ID], k) #get prefix of t
                if s_suffix == t_prefix: #if equal then add IDs to list
                    overlaps.append((s_ID, t_ID))
    return overlaps

def create_adjacency_list(adjacents):
    adj_list=[]
    for s, t in adjacents:
        adj_list.append(f"{s} {t}")
    return "\n".join(adj_list)

def main(fasta):
    adjacent = overlaps(fasta, k=3) #find adjacents by checking for overlaps
    return create_adjacency_list(adjacent)

print(main(fasta))
