store_inp = int(input())
inp_array = [0]*store_inp
inp_array[0] = 0
inp_array[1] = 1

for i in range(2, store_inp):
    if i%2 == 0:
        inp_array[i] = inp_array[int(i/2)]
    else:
        inp_array[i] = inp_array[int((i-1) / 2)] + inp_array[int((i+1) / 2)]

print(max(inp_array))