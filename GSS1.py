N = int(input())
inp_array = [int(x) if int(x) > 0 else 0 for x in input().split()]
M = int(input())
max_sum = [0]*M
indices = [[int(x) for x in input().split()] for i in range(M)]
for i in range(M):
    max_sum[i] = sum(inp_array[indices[i][0]-1:indices[i][1]])
    print(max_sum[i])
