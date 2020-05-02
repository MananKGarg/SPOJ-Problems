num = float(input())

while(not(num == 0)):
    length = 1/2
    cards = 1
    i = 3
    while(length<num):
        length = length + (1/i)
        cards = cards + 1
        i = i + 1

    print(cards, end=' ')
    print('card(s)')
    num = float(input())