# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 100001st prime number?

# Notice that all non-prime Numbers are divisible by either 2 or 3. Rule out primes 2 or 3 and any non primes below that value. All even numbers above 2 are divisible by 2 and can be disregarded. Then iterate through odd numbers above 3, and up to root of the given number(because if m*m=n then m is the max value of an possible divisor with remainder 0).


def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n < 2:
    return False
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  return True
  

def prime_in_sequence(seq_no):
  counter = 0
  prime_ = 0
  while prime_ < seq_no:
    counter += 1
    if is_prime(counter):
      prime_ += 1
    else:
      continue
  return counter

print(prime_in_sequence(10001))