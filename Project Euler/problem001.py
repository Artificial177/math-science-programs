# My original solution.
def sum_threefive(max_bound): # Problem #1

   result = 0

   for x in range(max_bound):
      if (x % 3 == 0):
         result += x
      elif (x % 5 == 0):
         result += x

   return result
   
print(sum_threefive(1000))

# One Line Optimized Solution
print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))
