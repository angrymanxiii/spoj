def num_zeros(num):
    nz = 0
    while num > 0:
        num = num // 5
        nz += num
    print(nz)


N = int(input())
inp_array = [int(input()) for x in range(N)]

for i in range(N):
    num_zeros(inp_array[i])
