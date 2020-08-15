try:
        for i in range(1024):
            n = input()

            if (int(n) == 1):
                print(n)
            elif(int(n) == 5):
                print("8")

            else:

                n_str = list(n)
                n_str.reverse()

                carry = 0

                for i in range(len(n_str)):

                    if (int(n_str[i]) < 5):
                        n_str[i] = str(2*(int(n_str[i])) + carry)
                        carry = 0

                    else:
                        n_str[i] = str(((2*(int(n_str[i]))) - 10) + carry)
                        carry = 1

                if (carry == 1):
                    n_str.append("1")

                if(int(n_str[0]) > 0):

                    n_str[0] = str(int(n_str[0]) - 2)

                else:
                    n_str[0] = "8"
                    l = 1
                    while( int(n_str[l]) == 0 ):
                        n_str[l] = "9"
                        l = l + 1
                    n_str[l] = str(int(n_str[l]) - 1)

                n_str.reverse()

                n_str = "".join(n_str)
                print(n_str)

except:
    pass

