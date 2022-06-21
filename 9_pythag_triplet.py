# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Remove as many dependant variables as poss for efficiency of search. n is known. Through rearranging we find:

# c = n - a - b
# b = n(n-2a) / 2(n-a)

# now we solve for a


import timeit as t
testcode = '''
def findTriplet(n):
  triplet = None
  for a in range(n//3-1, 2, -1):
    b = n*(n-2*a) // (2*(n-a))
    c = n - a - b
    if a < b and a*a + b*b == c*c:
      return (a, b, c)
  return triplet
'''


def findTriplet(n):
  triplet = None
  for a in range(n//3-1, 2, -1):
    b = n*(n-2*a) // (2*(n-a))
    c = n - a - b
    if a < b and a*a + b*b == c*c:
      return (a*b*c)
  return triplet

print(findTriplet(1000))
print(t.timeit(stmt=testcode))