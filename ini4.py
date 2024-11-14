#!/usr/bin/env python3

#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a=4352
b=8892

#create list of numbers between a and b
x = [*range(a, b+1)]
#find odd numbers between a and b
odd = []

for num in x:
    if num % 2 != 0:
        odd.append(num)

#sum odd numbers
print(sum(odd))