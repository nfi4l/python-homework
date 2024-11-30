 #!/usr/bin/env python3

def rabbits (n, k):
    if n<1:
        return 0
    if n==1 or n==2:
        return 1
    return rabbits (n-1, k) + k * rabbits (n-2, k) # recursion (with brakes defined above)

print(rabbits(35,3))