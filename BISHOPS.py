ls = []
while True:
    inp = input()
    if not inp:
        break
    ls.append(int(inp))

num_lines = len(ls)
for i in range(num_lines):
    if ls[i] == 1:
        print(1)
    else:
        print(2 * (ls[i] - 1))

