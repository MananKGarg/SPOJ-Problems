seq = input() # input is string

list = seq.split()  # splitting in string elements seperated by space
list = [int(i) for i in list] # list comprehension to convert str to int

while(not((list[0] == 0)and(list[1] ==0)and(list[2] == 0))):  # program terminates on [0,0,0]
    if(2*list[1] == list[0]+list[2]):                  # condition of AP
        print('AP', end=' ')
        print(list[2]+list[1] -list[0])                # T4 = T3 + (T2 - T1)

    else:                                              # either AP or GP is there in input
        print('GP', end=' ')
        print(int((list[2]*list[1])/list[0]))          # T4 = T3*T2/T1

    seq = input()                                      # next input
    list = seq.split()
    list = [int(i) for i in list]


