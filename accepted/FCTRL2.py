def fctrl(a, b):
    while b > 1:
        a *= b
        b -= 1

    return a, b


no_of_lines = int(input())
store_inp = []

for i in range(no_of_lines):
    store_inp.append(int(input()))

for i in range(no_of_lines):
    a, b = fctrl(1,store_inp[i])
    print(a)

