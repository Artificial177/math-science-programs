def circular_primes(input):
   primes = primes_range(input)
   print(primes)

   total = 0

   for prime_number in primes:
      if prime_number != 0:
         digits = [int(x) for x in str(prime_number)]
         trial_prime = True
         round_prime = []

         for value in range(len(digits)):
            new_list = digits[value:] + digits[:value]
            strings = [str(integer) for integer in new_list]

            aprime = ''.join(strings)
            aprime = int(aprime)
            round_prime.append(aprime)
            print(aprime)

            if aprime not in primes:
               trial_prime = False

         if trial_prime == True:
            total += 1

            if prime_number == 11:
               e = primes.index(11)
               primes[e] = 0
            else:
               for z in round_prime:
                  q = primes.index(z)
                  primes[q] = 0

   return total
   
print(circular_primes(1000000))
