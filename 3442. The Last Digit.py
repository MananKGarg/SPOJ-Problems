## Solution 1
t = int(input())

for i in range(t):
    seq = input()
    list = seq.split()
    list = [int(j) for j in list]
    
    if(list[1] == 0):
        print('1')
        
    else:

        ans = 1
        p = list[0]%10

        for k in range(list[1]):
            ans = ans * p
            ans = ans%10


        print(ans%10)

## Solution 2

t = int(input())

for i in range(t):
    seq = input()
    list = seq.split()
    list = [int(j) for j in list]

    if(list[1] == 0):
        print('1')
    elif(((list[0]%10) == (1 or 5 or 6 or 0))):
        print(list[0]%10)
    elif(((list[0]%10) == (4 or 9))):
        if(list[1]%2 == 1):
            print(list[0]%10)
        else:
            print(((list[0]%10)*(list[0]%10))%10)
    else:
        b = (list[1]%4)
        a = (list[0]*list[0]*list[0]*list[0])%10

        for k in range(b):
            a = a*list[0]

        print(a%10)
