#!/usr/bin/env python3

def count_occurences (x, l):
    counter = 0
    for num in l:
        if x == num:
            counter += 1
    return counter

# import file with two columns
with open("input/input_1.txt", "r") as file:
    locID1 = []
    locID2 = []
    for line in file:
        # split line by spaces to extract numbers
        num1, num2 = line.split()
        # put numbers into lists
        locID1.append(int(num1))
        locID2.append(int(num2))

# Part 1:
# pair up -> measure differences
# sort
s_loc1 = sorted(locID1) #or use locID1.sort()
s_loc2 = sorted(locID2)

# calculate distance
distances = []

for a, b in zip(s_loc1, s_loc2):
    difference = abs(a - b)
    distances.append(difference)

# print("distance:")
# print(*distances)
print("total distance:")
print(sum(distances))

# Part 2:

# figure out exactly how often each number from the left list appears in the right list -> count occurences
# calculate similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

col1 = locID1
col2 = locID2
similarity_index = []

for a in col1:
    occ_a = count_occurences(a, col2)
    similarity_index.append(a * occ_a)

print(sum(similarity_index))