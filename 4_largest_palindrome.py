# Question:

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# Palindrome checker function can accept string or integer input.

def is_palindrome(n):
  n_arr = [int(i) for i in str(n)]
  return n_arr == n_arr[::-1]


def largest_pal(n1, n2):
  palindrome = float('-inf')
  for i in range(100, 1000):
    for j in range(100, 1000):
      prod = i * j
      if is_palindrome(prod):
        if prod > palindrome:
          palindrome = prod
  if palindrome == '-inf':
    return None
  else:
    return palindrome


#Driver Code
print(largest_pal(999, 999))
