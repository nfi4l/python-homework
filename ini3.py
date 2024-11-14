#!/usr/bin/env python3

#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

s="crtt8NLuMFRPQoEibekcKJYyVYXLzazoHCPJyYGPoM0gumPhylloscopus48pv3Avz2IJGeSstZ4AiAFoZDOKQoVyiILXsmaragdinaR4wKCgaval1mjlFNjJEySOHJZcJmFIBeoHzFPaQHkDgrVMGu8TUzBJfOeHWxTxDZnZy9DiVE5Rf53ZxHHFBY4T."

a=46
b=57
c=93
d=102

s_slice1=s[a:b+1]
s_slice2=s[c:d+1]

print(s_slice1, s_slice2)

#Solution: Phylloscopus smaragdina