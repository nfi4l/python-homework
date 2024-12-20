#!/usr/bin/env python3

# Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

from util import read_input #import read_input function from util.py

# read file
inp = "../rosalind_data/rosalind_ini5.txt"
lines = read_input(inp)
#with open(filepath, "r") as infile:
#    lines = infile.readlines()

#print only even-numbered lines
for l in lines[1::2]:
    print(l.strip())
    

#Solution:
#Some things in life are bad, they can really make you mad
#Other things just make you swear and curse
#When you're chewing on life's gristle, don't grumble give a whistle
#This will help things turn out for the best
#Always look on the bright side of life
#Always look on the right side of life
#If life seems jolly rotten, there's something you've forgotten
#And that's to laugh and smile and dance and sing
#When you're feeling in the dumps, don't be silly, chumps
#Just purse your lips and whistle, that's the thing
#So, always look on the bright side of death
#Just before you draw your terminal breath
#Life's a counterfeit and when you look at it
#Life's a laugh and death's the joke, it's true
#You see, it's all a show, keep them laughing as you go
#Just remember the last laugh is on you
#Always look on the bright side of life
#And always look on the right side of life
#Always look on the bright side of life
#And always look on the right side of life