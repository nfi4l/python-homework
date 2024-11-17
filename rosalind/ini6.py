#!/usr/bin/env python3

#Given: A string s of length at most 10000 letters.
#Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

#import file
filepath = "../rosalind_data/rosalind_ini6.txt"
with open(filepath, "r") as imp:
    s = imp.read()

words_s = s.split() # split everything into words

dict_count={}

#loop to check if word from words_s is already in dictionary, if yes then add ontop, if not add word to dictionary
for word in words_s:
    if word in dict_count:
        dict_count[word] += 1
    else:
        dict_count[word] = 1

#print words and numbers
for word, num in dict_count.items():
    print(word, num)