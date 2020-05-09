n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list.sort()

if(len(num_list) == 1):
    print(num_list[0])

elif(num_list[-1] != num_list[-2]):
    print(num_list[-1])
else:
    for j in range(0,n-2,2):
        if(num_list[j] != num_list[j+1]):
            print(num_list[j])
            break


