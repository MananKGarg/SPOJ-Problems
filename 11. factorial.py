t = int(input())

for i in range(t):
    num = int(input())

    p = 5               # number of fived determine number of zeroes in factorial
    add = num//p        # 0's = [n/5] + [n/25] + [n/125] ...
    zero_count = 0
    while(add>0):
        zero_count = zero_count + add
        p = p*5
        add = num//p
    print(zero_count)
