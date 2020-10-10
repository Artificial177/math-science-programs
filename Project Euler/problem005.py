def smallest_multiple(bound): # Problem 5
   mul = 1
   for i in range(2, bound + 1):
      mul *= i // math.gcd(i, mul)

   return mul

print(smallest_multiple(20))
