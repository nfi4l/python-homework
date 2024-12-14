#!/usr/bin/env python3

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k=16
m=15
n=21
S=k+m+n #population

lala = (k/S) + (m/S)*((4*k + 3*m-3 + 2*n)/(4*(S-1))) + (n/S)*((2*k+m)/(2*(S-1)))

print(lala)