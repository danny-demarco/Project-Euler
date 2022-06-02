
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def primeFactor(given):
  factors = []

  # Find factors of 2
  while given % 2 == 0:
    given = given / 2
    factors.append('2')
  
  # Remaining number is now odd
  for number in range(3, int(math.sqrt(given))+1, 2):
    while given % number == 0:
      factors.append(number)
      given = given / number

  # If given number is prime
  if given > 2:
    factors.append(given)
  return factors



#Driver (Gives largest prime only)
given = 600851475143
print(max(primeFactor(given)))



      
