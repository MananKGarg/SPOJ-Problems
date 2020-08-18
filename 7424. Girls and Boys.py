import math
girls, boys = [int(i) for i in input().split()]

while ((girls != -1) and (boys != -1)):
    if (girls > boys):
        print(math.ceil(girls/(boys + 1)))

    else:
        print(math.ceil(boys/(girls + 1)))

    girls, boys = [int(j) for j in input().split()]