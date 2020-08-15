"""
https://projecteuler.net/problem=6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

d = sum([i for i in range(1, 101)]) ** 2 - sum([i ** 2 for i in range(1, 101)])

print(d)
