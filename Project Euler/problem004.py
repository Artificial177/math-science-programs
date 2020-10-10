def largest_palindrome_product():
   max = 0
   for i in range(100, 1000):
      print(i)
      for j in range(100, 1000):
         if str(i * j) == str(i * j)[::-1]:
            if i * j > max:
               max = i * j

   return max

print(largest_palindrome_product())
