def fib(limit):
  if limit <= 1:
    return limit
  else:
    return fib(limit-1) + fib(limit-2)

# Driver Code
# limit = int(input("Give fib sequence number... "))
limit = 34
sequence = [fib(i) for i in range(limit)]
evens = [x for x in sequence if x % 2 == 0]

print(sequence)
print(sum(evens))
