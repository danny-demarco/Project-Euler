# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Notice** question is asking for the LCM of a series of numbers.

#LCM(a,b)=a×b / GCD(a,b)
# lcm(a,b,c) = lcm(lcm(a,b), c)  => reduce() function can be used.

import math
import functools

def lcm(a,b):
  return a*b//math.gcd(a,b)

lcm_ans = functools.reduce(lcm, range(1, 20+1))

print(lcm_ans)