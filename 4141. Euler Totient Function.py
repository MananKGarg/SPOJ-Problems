import math


def PrimeFactors(n):
    prime_factors = []

    if (n % 2 == 0):
        prime_factors.append(2)
        while (n % 2 == 0):
            n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            prime_factors.append(i)
            while (n % i == 0):
                n = n / i

    if (n > 2):
        prime_factors.append(n)

    return prime_factors


#Solution 1
"""
def gcd(a,b):
    if(a == 0):
        return b
    return gcd(b%a,a)

t = int(input())

for i in range(t):
    n = int(input())
    count = 0
    for j in range(1,n+1):
        if(gcd(j,n) == 1):
            count = count + 1
    print(count)
"""
#Solution 2

t = int(input())

for i in range(t):
    num = int(input())
    list = PrimeFactors(num)

    for j in range(len(list)):
        num = num * (1 - (1/list[j]))

    print(int(num))

