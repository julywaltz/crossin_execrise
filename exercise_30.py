from math import sqrt

primes = []
for num in range(1,100000000):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end+1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        primes.append(num)
print(primes)