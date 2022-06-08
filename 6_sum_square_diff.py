# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2 = 385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 55^2 =3052

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def diff(n):
  sum_of_squares = sum([i**2 for i in range(n+1)])
  square_of_sums = (sum(range(n+1)))**2
  return square_of_sums - sum_of_squares

print(diff(100))