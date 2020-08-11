"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def get_biggest_divisor(n):
  for i in range(998, 99, -1):
    if n % i == 0:
      return  i
  return -1

def is_palindrome(n):
  n_string = str(n)
  number_of_digits = len(n_string)

  if number_of_digits % 2 == 1:
    digits_to_compare = int((number_of_digits - 1) / 2)
  else:
    digits_to_compare = int(number_of_digits / 2)

  for i in range(digits_to_compare):
    if n_string[i] != n_string[-1 - i]:
      return False

  return True

i = 999 * 999

while True:
  if is_palindrome(i):
    d = get_biggest_divisor(i)
    if d > 0:
      r = int(i / d)
      if len(str(r)) == 3:
        print(i)
        break
  i -= 1
