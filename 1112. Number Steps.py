t = int(input())

for j in range(t):
    seq = input()
    list = seq.split()
    list = [int(i) for i in list]

    x = list[0]
    y = list[1]

    if(x==y):
        if(x%2 == 0):
            print(2*x)
        else:
            print(2*x-1)

    elif((x-y)==2):
        if(x%2==0):
            print(2*x-2)
        else:
            print(2*x-3)
    else:
        print('No Number')

