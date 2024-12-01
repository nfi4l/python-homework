#!/usr/bin/env python3

#import file with two columns
with open("input/input_1.txt", "r") as file:
    locID1 = []
    locID2 = []
    for line in file:
        # split line by spaces to extract numbers
        num1, num2 = line.split()
        # put numbers into lists
        locID1.append(int(num1))
        locID2.append(int(num2))

#pair up -> measure differences

#sort
s_loc1 = sorted(locID1)
s_loc2= sorted(locID2)

#calculate distance
distances = []

for a, b in zip(s_loc1, s_loc2):
    difference = abs(a - b)
    distances.append(difference)

# print("distance:")
# print(*distances)
print("total distance:")
print(sum(distances))
