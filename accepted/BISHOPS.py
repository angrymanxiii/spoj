ls = []
try:
    inp = input()
    while 1 <= int(inp) <= 1e100:
        ls.append(int(inp))
        inp = input()
except:
    num_lines = len(ls)
    for i in range(num_lines):
        print(max(1,2 * (ls[i] - 1)))
