def merge(b,c):
    d =[]

    while((len(b) != 0) and ((len(c)) != 0)):

        if( b[0] <= c[0] ):
            d.append(b[0])
            b.pop(0)

        else:
            d.append(c[0])
            c.pop(0)

    if(len(b) == 0):
        d.extend(c)
    else:
        d.extend(b)

    return d

def mergesort(arr):

    if (len(arr) == 1):
        return arr

    m = len(arr)//2
    left = arr[:m]
    right = arr[m:]

    l = mergesort(left)
    r = mergesort(right)

    ans = merge(l,r)
    return ans



arr = [int(i) for i in input().split()]


print(arr)
print(mergesort(arr))
