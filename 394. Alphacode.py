n = input()

while (int(n) != 0):

    p = []
    p.append(0)
    p.append(1)

    l = len(n)

    if (l < 2):
        print(p[1])

    else:
        t_digit = int(n[0])*10 + int(n[1])

        if ((int(n[1]) == 0) and (t_digit < 27)):
            p.append(1)
        elif ((int(n[1] == 0)) and (t_digit > 26)):
            p.append(0)
        elif ((int(n[1]) != 0 ) and (t_digit < 27)):
            p.append(2)
        elif ((int(n[1] != 0)) and (t_digit >26)):
            p.append(1)



        for i in range(3,l+1):

            two_digit = int(n[i-2]) * 10 + int(n[i-1])

            if ((int(n[i-1]) == 0) and (two_digit < 27)):
                p.append(p[i-2])
            elif ((int(n[i-1]) != 0) and (two_digit < 27) and (int(n[i-2]) == 0)):
                p.append(p[i-1])
            elif ((int(n[i - 1]) != 0) and (two_digit < 27) and (int(n[i - 2] != 0))):
                p.append(p[i - 1] + p[i - 2])
            elif ((int(n[i-1]) != 0) and (two_digit > 26) and (int(n[i-2]) == 0)):
                p.append(0)
            elif ((int(n[i - 1]) != 0) and (two_digit > 26) and (int(n[i - 2]) != 0)):
                p.append(p[i-1])

        print(p[-1])

    n = input()




















