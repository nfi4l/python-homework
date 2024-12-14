#!/usr/bin/env python3

#Given: A DNA string of length at most 1 kbp in FASTA format.
#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

from util import read_input

inp = "../rosalind_data/rosalind_revp.txt"
fasta = read_input(inp)

seq = ""

for line in fasta:
    if line.startswith(">"):
        continue
    else:
        seq += line

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
    
def reverse_complement(seq):
    comp = ""
    for base in seq[::-1]:
        comp += complement(base)
    return comp


def is_palindrome(seq, i, length):
    test = seq[i:i+length]
    if reverse_complement(test) == test:
        return True
    return False

def main():
    #goblin was here
    for window_size in range (4, 13, 2):
        for i in range(0, len(seq)-(window_size-1)):
            if is_palindrome(seq, i, window_size):
                print(i+1, window_size)


if __name__ == "__main__":
    main()