"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
  for i in range(3, n):
    if n % i == 0:
      return False
  return True

i = 3
target = 10001
prime_counter = 2

while True:
  if is_prime(i):
    if prime_counter == target:
      print(i)
      break
    prime_counter += 1
  i += 2
