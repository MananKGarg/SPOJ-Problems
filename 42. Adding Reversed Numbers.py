def reverse(number):
    rev = 0

    while(number>0):
        p = number%10
        rev = rev*10 + p
        number = number//10

    return rev


t = int(input())

for j in range(t):
    seq = input()
    list = seq.split()
    list = [int(i) for i in list]

    print(reverse(reverse(list[0])+reverse(list[1])))
