def sum_of_characters_in_words(num):
   tot = 0
   for number in range(1, num + 1):
      z = [char for char in num2words(number)]
      for char in z:
         if char == ' ' or char == '-':
            z.pop(z.index(char))
      print(z)
      tot += len(z)

   return tot
