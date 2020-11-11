def large_fib():
   # Solved through recursive generation of the Fibonacci Numbers.
   def fib():
      a = 0
      b = 1
      while True:
         yield a
         a, b = b, a + b

   for index, number in enumerate(fib()):
      if len(str(number)) == 1000:
         print(index)
         break

print(large_fib())

