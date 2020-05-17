# Solution 1

cols = int(input())

while(cols != 0):

    string = input()
    ans = ""

    for j in range(cols):
        for i in range(0, ((int(len(string)/cols) * cols) - (2 * cols) + 1), (cols * 2)):
            ans += string[i + j] + string[i - j - 1 + (2 * cols)]
            
    print(ans)

