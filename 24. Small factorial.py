t = int(input())

for i in range(t):
    num = int(input())
    j = 1
    fact = 1
    while(j<num+1):
        fact = fact*j
        j = j + 1

    print(fact)
