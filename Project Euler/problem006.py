def sum_square_difference(input):
   rangex = input
   square_sum = 0
   sum_square = 0


   for x in range(1, rangex+1):
      print(x)
      sum_square += x**2
      square_sum += x

   square_sum = square_sum**2

   return square_sum-sum_square
   
   
