n = int(input())

while(n != -1):
    no_candies = []
    for i in range(n):
        no_candies.append(int(input()))
    if(sum(no_candies) % n == 0):
        candy_bag = sum(no_candies) // n
        count = 0
        for j in no_candies:
            if(j>candy_bag):
                count = count + (j - candy_bag)
        print(count)

    else:
        print("-1")

    n = int(input())
