"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = 600851475143
r = n

for i in range(2, n):
    if is_prime(i):
        if n % i == 0:
            r /= i
            if r == 1.0:
                print(i)
                break
