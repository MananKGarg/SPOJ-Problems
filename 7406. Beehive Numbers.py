n = int(input())

while(not(n == -1)):

    t = 1
    bn = 1

    while(bn<n):
        bn = bn + 6*t
        t = t + 1


    if(bn == n):
        print('Y')
    else:
        print('N')

    n = int(input())
