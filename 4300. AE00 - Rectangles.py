import math

def num_factors(n):

    num_factors = []
    num = n

    if(num%2 == 0):
        count2 = 0
        while(num%2 == 0):
            count2 += 1
            num = num/2
        num_factors.append(count2 + 1)

    for i in range(3, int(math.sqrt(n) + 2), 2):

        if(num%i == 0):
            counti = 0
            while( num%i == 0):
                counti += 1
                num = num/i
            num_factors.append(counti + 1)

        else:
            pass
    if(num > 2):
        num_factors.append(2)

    prod = 1
    for u in num_factors:
        prod = prod*u

    if(prod%2==0):
        return prod//2
    else:
        return ((prod//2) + 1)


t = int(input())
if(t==0):
    print("0")
else:
    rects = 1
    for l in range(t,1,-1):
        rects = rects + num_factors(l)
    print(rects)
