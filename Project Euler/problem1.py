def sum_threefive(max_bound): # Problem #1

   result = 0

   for x in range(max_bound):
      if (x % 3 == 0):
         result += x
      elif (x % 5 == 0):
         result += x

   return result
   
print(sum_threefive(1000)
