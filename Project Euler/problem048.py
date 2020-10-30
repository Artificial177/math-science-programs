def self_powers(input_num, x): #Problem 48
   sum = 0

   for t in range(1, input_num+1):
      sum += (t**t)


   if x == 2:
      z = [int(z) for z in str(sum)]

      z = z[-10:]

      return ''.join(str(z))

   return sum

print(self_powers(1000, 2))

