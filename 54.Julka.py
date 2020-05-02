# Solution 1

for i in range(10):
    num = int(input())
    more = int(input())

    nat = int((num-more)/2)
    kla = nat + more

    print(kla)
    print(nat)

# Solution 2

for i in range(10):
    num = int(input())
    more = int(input())

    num = num + more
    ans = num//2
    print(ans)
    print(ans-more)