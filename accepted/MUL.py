N = int(input())
inp_array = [0]*N
prod = [0]*N
for i in range(N):
    inp_array[i] = [int(x) for x in input().split()]
    prod[i] = inp_array[i][0] * inp_array[i][1]

for i in range(N):
    print(prod[i])
