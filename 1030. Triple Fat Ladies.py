## Solution 1
t = int(input())

for i in range(t):
    k = int(input())
    list = []
    p = 192

    while(len(list)<k):
        cube = p*p*p
        if(cube%1000 == 888):
            list.append(p)
        p = p + 10

    print(list[-1])

## Solution 2

t = int(input())

for i in range(t):
    k = int(input())
    ans = 192 + (k-1)*250
    print(ans)
