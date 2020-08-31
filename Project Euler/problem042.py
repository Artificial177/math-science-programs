def coded_triangle_numbers():
   f = open("euler42_words.txt").read()
   f = f.split('","')

   def check_num(input_str):
      letters = input_str

      if letters.startswith('"'):
         letters = letters[-1:]
      if letters.endswith('"'):
         letters = letters[:-1]


      triangle_numbers = []
      for x in range(1, 26):
         z = int(0.5 * (x * (x + 1)))
         triangle_numbers.append(z)

      insum = 0

      for letter in letters:
         number = ord(letter) - 64
         insum += number

      if insum in triangle_numbers:
         return True
      else:
         return False

   sum_of_num = 0

   for item in f:
      t = check_num(item)

      if t == True:
         sum_of_num += 1

   return sum_of_num
