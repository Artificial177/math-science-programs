def power_digit_sum():
   num = 2 ** 1000
   tot = 0
   while num >= 1:
      temp = num % 10
      tot = tot + temp
      num //= 10
   return tot

print(power_digit_sum())
