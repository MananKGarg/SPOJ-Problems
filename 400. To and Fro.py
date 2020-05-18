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
