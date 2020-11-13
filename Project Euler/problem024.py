from itertools import permutations

def lexiographic(num, index): # Problem 24
   d = list(int(''.join(p)) for p in permutations(str(num)))
   d.sort()

   return d[index - 1]

print(lexiographic(1234567890, 1000000))
