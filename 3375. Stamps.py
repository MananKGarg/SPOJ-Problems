t = int(input())

for i in range(t):

    first = input().split()
    stamps_needed = int(first[0])
    friends = int(first[1])

    stamps = [int(j) for j in input().split()]

    stamps.sort( reverse = True)

    if (sum(stamps) < stamps_needed):
        print("Scenario #", end="")
        print(i+1,end="")
        print(":")
        print("impossible")
        print("")

    else:
        k = 0
        count = 0
        tot = 0

        while (tot < stamps_needed):

            tot = tot + stamps[k]
            count = count + 1
            k = k + 1


        print("Scenario #", end="")
        print(i+1,end="")
        print(":")
        print(count)
        print("")