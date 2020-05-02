# Solution 1

t = int(input())
for i in range(t):
    n = int(input())
    if(n==1):
        print('1')
    elif(n==2):
        print('5')
    elif(n==3):
        print('13')
    else:
        count = 4
        for j in range(3,n-1):
            count = count + j*j - j

        count = count + n*n + (n-1)*(n-1) - (n-2)
        print(count)


# Solution 2

t = int(input())
for i in range(t):
    n = int(input())
    print((((n)*(n+2)*(2*n+1))//8))
