def name_score():
   f = open("p022_names.txt").read() # Replace the text file name with the name of the local file.
   f = f.split('","')


   new_file = []

   def replace_item(input_str):
      letters = input_str
      letterx = [str(z) for z in str(letters)]

      if letterx[0] == '"':
         del letterx[0]
      if letterx[-1] == '"':
         del letterx[-1]

      letterq = ''.join(letterx)

      return letterq

   for item in f:
      new_file.append(replace_item(item))

   new_file.sort()

   def give_score(input_str):
      letters = input_str

      insum = 0

      for letter in letters:
         number = ord(letter)-64
         insum += number

      #print(insum)
      return insum

   totsum = 0
   list_count = 1

   for item in new_file:
      if list_count == 938:
         print(item)

      totsum += list_count * give_score(item)
      list_count += 1

   return totsum
