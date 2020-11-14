def to_decimal(num, den):
   res = ""
   mp = {}

   rem = num % den

   while((rem != 0) and (rem not in mp)):
      mp[rem] = len(res)
      rem *= 10
      part = rem // den
      res += str(part)
      rem %= den

   if rem == 0:
      return ""
   else:
      return res[mp[rem]:]

max = 0
maxnum = 0
for i in range(1, 1000):
   if len(to_decimal(1, i)) > max:
      max = len(to_decimal(1, i))
      maxnum = i

print(maxnum)
