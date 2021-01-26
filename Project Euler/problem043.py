from itertools import permutations

list_o_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

nums = permutations(list_o_nums)

sum = 0
for num in nums:
   num1 = int(''.join(num[1:4]))
   if num1 % 2 == 0:
      num2 = int(''.join(num[2:5]))
      if num2 % 3 == 0:
         num3 = int(''.join(num[3:6]))
         if num3 % 5 == 0:
            num4 = int(''.join(num[4:7]))
            if num4 % 7 == 0:
               num5 = int(''.join(num[5:8]))
               if num5 % 11 == 0:
                  num6 = int(''.join(num[6:9]))
                  if num6 % 13 == 0:
                     num7 = int(''.join(num[7:10]))
                     if num7 % 17 == 0:
                        sum += int(''.join(num))

print(sum)
