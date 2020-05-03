import math

def PrimeFactors(n):
    prime_factors = []

    if(n%2 == 0):
        prime_factors.append(2)
        while(n%2 == 0):
            n = n/2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if(n%i == 0):
            prime_factors.append(i)
            while(n%i == 0):
                n = n/i

    if (n>2):
        prime_factors.append(n)

    return prime_factors

