# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Take function is_prime() designed in 7 to check if prime:

allPrimes = []

def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n < 2:
    return False
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def findPrimes(n):
  for i in range(n+1):
    if is_prime(i):
      allPrimes.append(i)
  return allPrimes

print(sum(findPrimes(2000000)))

