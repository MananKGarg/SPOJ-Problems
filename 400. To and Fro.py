# Solution 1

cols = int(input())

while(cols != 0):

    string = input()
    ans = ""

    for j in range(cols):
        for i in range(0, ((int(len(string)/cols) * cols) - (2 * cols) + 1), (cols * 2)):
            ans += string[i + j] + string[i - j - 1 + (2 * cols)]
            
    print(ans)

# Solution 2

import numpy as np
cols = int(input())

while(cols != 0):

    string = input()
    arr = np.array(list(string))
    print(arr.size)
    arr = arr.reshape(int(len(string)/cols), cols)
    arr[1::2, :] = arr[1::2, ::-1]
    arr = arr.flatten('F')
    listToStr = ''.join([str(elem) for elem in arr])
    
    print(listToStr)

    
    
    
# Solution 3

while(1):
    n = int(input())
    if n==0:
        break
    s = input()
    if n==1:
        print(s)
    else:
        s_list = []
        s_list = [s[i:i+n][::-1] if ((i/n)%2)!=0 else s[i:i+n] for i in range(0, len(s), n)]
        s= ""
        for i in range(0,n):
            for x in s_list:
                try:
                    s = s+ x[i]
                except:
                    pass
        print(s)    
    
    
