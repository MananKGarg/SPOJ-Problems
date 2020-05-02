t = int(input())

for i in range(t):
    seq = input()
    list = seq.split()
    list = [int(j) for j in list]

    t3,tn3,sum = list

    n = (2*sum)//(t3 + tn3)
    print(n)

    d = (tn3-t3)//(n-5)
    a = t3 - 2*d


    for k in range(n):
        print(a,end=' ')
        a = a + d
