import math
l = int(input())

while(l != 0):
    print("{0:.2f}".format((l*l)/(2*(math.pi))))
    l = int(input())