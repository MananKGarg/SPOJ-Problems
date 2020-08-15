try:
    n = input()
    while (int(n) > 0):

        if (int(n) == 1):
            print(n)
        elif (int(n) == 5):
            print("8")

        else:

            n_str = list(n)        # convert string to list of characters (digits)
            n_str.reverse()

            carry = 0

            for i in range(len(n_str)):

                if (int(n_str[i]) < 5):
                    n_str[i] = str(2 * (int(n_str[i])) + carry)      # if n_str[i] == 4, then 2n have 8 in the corresponding position
                    carry = 0

                else:
                    n_str[i] = str(((2 * (int(n_str[i]))) - 10) + carry)   # if n_str[i] == 6, then 2n, will be 12, but only two would remain and one would go as carry
                    carry = 1

            if (carry == 1):
                n_str.append("1")

            if (int(n_str[0]) > 0):

                n_str[0] = str(int(n_str[0]) - 2)   # if the last digit is greater then 0

            else:
                n_str[0] = "8"                      # if last digit is equal to 0
                l = 1
                while (int(n_str[l]) == 0):
                    n_str[l] = "9"
                    l = l + 1
                n_str[l] = str(int(n_str[l]) - 1)

            n_str.reverse()

            n_str = "".join(n_str)                  # make a string again
            print(n_str)

        n = input()
except:
    pass












