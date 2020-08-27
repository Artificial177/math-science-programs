def evensum_fib(max_bound): # Problem #2
   num1 = 1
   num2 = 1
   num3 = num1 + num2

   even_sum = 0
   recursive = 0

   while num3 < max_bound:
      if recursive != 0:
         num2 = num1
         num1 = num3

      num3 = num1 + num2

      if(num3 % 2 == 0):
         if (num3 < max_bound):
            even_sum += num3

      recursive += 1

   return even_sum

print(evensum_fib(4000000))
