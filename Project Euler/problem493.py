def under_rainbow():
   prob = float(1.0)
   for i in range(20):
      prob *= round(float((60 - i) / (70 - i)), 10)

   return (round((1 - prob) * 7, 9))

print(under_rainbow())
