def largest_collatz(input):
   max_range = input

   def term_calc(n):
      seq = True
      term_amount = 0

      while seq == True:
         if n == 1:
            seq = False
         else:
            if n % 2 == 0:
               n = n / 2
            else:
               n = 3 * n + 1
         term_amount += 1

      print(term_amount)
      return term_amount

   greatest = 1
   greatest_num = 1

   for x in range(2, input+1):
      print(x)
      new_num = term_calc(x)

      if new_num > greatest:
         greatest = new_num
         greatest_num = x


   return greatest_num
   
print(largest_collatz(1000000))
