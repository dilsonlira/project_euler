"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def get_divisors(n, divisors=None):
  if divisors is None:
    divisors = {}
  for i in range(2, n + 1):
    if n % i == 0:
      if i in divisors:
        divisors[i] += 1
      else:
        divisors[i] = 1
      if i < n:
        return get_divisors(int(n / i), divisors)
      else:
        return divisors

all_divs = get_divisors(20)
for i in range(19, 1, -1):
  i_divs = get_divisors(i)
  for j in i_divs:
    if j in all_divs:
      if i_divs[j] < all_divs[j]:
        continue
    all_divs[j] = i_divs[j]

n = 1
for k in all_divs:
  n *= int(k ** all_divs[k])

print(n)
