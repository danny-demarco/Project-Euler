def sumMultiples(upper_limit):
   multip = [i for i in range(upper_limit) if i % 3 == 0 or i % 5 == 0]
   return sum(multip)


print(sumMultiples(1000))