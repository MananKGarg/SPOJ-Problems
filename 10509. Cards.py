t = int(input())

for i in range(t):

    n = int(input())
    ans = int((n * (3*n + 1)) / 2)
    print(ans % 1000007)