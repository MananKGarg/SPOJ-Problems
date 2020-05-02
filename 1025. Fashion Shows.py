t = int(input())

for i in range(t):
    n = int(input())

    seq1 = input()
    men = seq1.split()
    men = [int(j) for j in men]
    men.sort()

    seq2 = input()
    women = seq2.split()
    women = [int(k) for k in women]
    women.sort()

    sum = 0
    for a in range(n):
        sum = sum + (men[a]*women[a])

    print(sum)

