def product_in_series(input, adj):
   num = input

   num_list = [int(x) for x in str(num)]
   greatest_product=0
   recursive_product=1

   list_len = len(num_list)

   q = 0

   for x in range(0, (list_len-adj)):
      recursive_product = 1
      for z in range(q, q + adj):
         recursive_product *= num_list[z]
      print()
      q += 1

      if recursive_product > greatest_product:
         greatest_product = recursive_product


   return greatest_product
