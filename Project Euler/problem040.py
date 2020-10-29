def champernowe():
   num_list = []
   z = []

   final = 1

   for num in range(1, 1000001):
      if num >= 10:
         z = [int(x) for x in str(num)]

         for value in z:
            num_list.append(value)

      else:
         num_list.append(num)

   tracker = [1, 10, 100, 1000, 10000, 100000, 1000000]

   for value in tracker:
      final *= num_list[value-1]
      print(value)
      print(final)

   return final
   
champernowe()
