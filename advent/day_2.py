#!/usr/bin/env python3

# Part 1:

# find safe reports
# safe criteria:
# - all increase or decrease -> no fluctuation
# - distance adjacent levels differ by at least one and at most three -> range[1,3]

# Part 2:

# Implement Problem Dampener -> if removing a single level from an unsafe report would make it safe, the report instead counts as safe
# check how many False statements there are  -> if <= 1 False -> True = Problem Dampener -> safe = True

# ID1 = [7, 6, 4, 2, 1]
# ID2 = [1, 2, 7, 8, 9]
# ID3 = [9, 7, 6, 2, 1]
# ID4 = [1, 3, 2, 4, 5]
# ID5 = [8, 6, 4, 4, 1]
# ID6 = [1, 3, 6, 7, 9]

# reports = [ID1, ID2, ID3, ID4, ID5, ID6]


def extract_rows(filepath):
    row_lists = []
    with open(filepath, 'r') as file:
        for line in file:
            stripped_line = line.strip() #remove spaces
            # split line into separate strings by spaces
            split_line = stripped_line.split()
            # convert str to int
            row = []
            for num in split_line:
                row.append(int(num))
            # add row to the list of rows
            row_lists.append(row)
    return row_lists

reports = extract_rows("input/input_2.txt")
# print(reports)



def descending_or_ascending (ID):
    descending = True
    ascending = True
    for i in range(len(ID)-1):
        if ID[i] < ID[i+1]:
             descending = False
             #des_f_count += 1
        elif ID[i] > ID[i+1]:
             ascending = False
             #asc_f_count += 1
             #goblin was here

    if descending:
        return descending #-> safe
    elif ascending:
        return ascending #-> safe
    else:
        return False

def is_fluctuating (ID):
    #false_count = 0
    for i in range(len(ID)-1):
        distance = abs(ID[i]-ID[i+1])
        if distance < 1 or distance > 3:
            return False
    return True



#check how many lists are safe
safe = 0

# print(descending_or_ascending(ID1))
# print(is_fluctuating(ID1))

# if descending_or_ascending(ID1) and is_fluctuating(ID1) == True:
#     safe += 1

# print(safe)


for ID in [*reports]:
    # print(f"des/asc: {descending_or_ascending(ID)}")
    # print(f"fluct: {is_fluctuating(ID)}")
    if descending_or_ascending(ID) and is_fluctuating(ID) == True:
        safe += 1
    else:
        # loop over reports that are one level shorter
        for i in range(len(ID)):
            shorter = ID[:i] + ID[i+1:]
            #print(shorter)
            if descending_or_ascending(shorter) and is_fluctuating(shorter) == True:
                safe += 1
                break

print(f"safe reports: {safe}")