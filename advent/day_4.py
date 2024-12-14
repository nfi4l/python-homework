#!/usr/bin/env python3

# find word horizontally, vertically, diagonally, backwards and in overlaps

def read_input(filepath):
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

list_rows = read_input("input/input_4.txt")

print(list_rows)

#==========================

#count horizontally
def find_horizontal(word, text):
    total_occurences = 0
    for line in text:
        total_occurences += line.count(word)
    return total_occurences

#count vertically
#flip text -> search for horizontal matches in flipped text
#swap indices!
def flip(text):
    columns = [""] * len(text)#creates columns from number of rows
    for line in text:
        #have to go over all characters in this line and put each character in its corresponding row in the flipped text
        for i, letter in enumerate(line): #enumerate -> makes indices of characters
            columns[i] += letter
    return columns

def find_vertical (word, text):
    flipped = flip(text)
    occurences = find_horizontal(word, flipped)
    return occurences

#count diagonally
#same concept
def dr_diag_starts(n):
    # find all starting positions for diagonals that go downwards and to the right
    diag = []
    for i in range(n):
        diag.append([i,0]) #add 0,0 1,0 2,0 ...
    for j in range(1, n): #leave out 0,0
        diag.append([0,j]) #add 0,0 0,1 0,2 ...
    return diag

def dr_diag(text, start):
    i = start[0]
    j = start[1]
    n = len(text)
    diag = ""
    while i < n and j < n: # do this as long as conditions are true
        diag += text[i][j]
        i += 1
        j += 1
    return diag

def find_diagonal_dr(word, text):
    dr_starts = dr_diag_starts(len(text))
    dr_diagonals=[]
    for start in dr_starts:
        diagonal = dr_diag(text, start)
        dr_diagonals.append(diagonal)
    occ = find_horizontal(word, dr_diagonals)
    return occ

def mirror(text):
    mirrored = []
    for line in text:
        mirrored.append(line[::-1])
    return mirrored

def find_diagonal_dl(word, text):
    mirrored = mirror(text)
    occ = find_diagonal_dr(word, mirrored)
    return occ

#==========================
#horizontal
hor_forw = find_horizontal("XMAS", list_rows)
hor_back = find_horizontal("SAMX", list_rows)
#vertical
vert_forw = find_vertical("XMAS", list_rows)
vert_back = find_vertical("SAMX", list_rows)
#diagonal
#down right
dr_forw = find_diagonal_dr("XMAS", list_rows)
dr_back = find_diagonal_dr("SAMX", list_rows)
#down left
dl_forw = find_diagonal_dl("XMAS", list_rows)
dl_back = find_diagonal_dl("SAMX", list_rows)

total = vert_forw + vert_back + hor_back + hor_forw + dr_back + dr_forw + dl_back + dl_forw
print(total)

#part 2: find MAS in X arrangement, forward or backward

def xmas(text, i, j):
    # find x mas around A
    diag_a = text[i-1][j-1] + text[i][j] + text[i+1][j+1]
    diag_b = text[i-1][j+1] + text[i][j] + text[i+1][j-1]

    diag_a_mas = diag_a == 'MAS' or diag_a == 'SAM'
    diag_b_mas = diag_b == 'MAS' or diag_b == 'SAM'
    if diag_a_mas and diag_b_mas:
        return True
    return False

total_mas = 0
for i in range(1, len(list_rows)-1):#start at middle for i
    for j in range(1, len(list_rows)-1):#start at middle for j
        if list_rows[i][j] == 'A':
            total_mas += xmas(list_rows, i, j)

print(total_mas)