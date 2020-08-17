"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(n):
    if n < 2:
        return False
        
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True
  
         
sum_of_primes = 2
for i in range(3, 2000000, 2):
    if is_prime(i):
        sum_of_primes += i
print(sum_of_primes)
