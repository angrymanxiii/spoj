ls = []
try:
    inp = input()
    while int(inp) >= 0:
        ls.append(int(inp))
        inp = input()
except:
    num_lines = len(ls)
    for i in range(num_lines):
        if ls[i] % 2 == 0:
            print(ls[i]//2)
        else:
            print(ls[i]//2 - ls[i])
