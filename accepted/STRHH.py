def first_half(str):
    l = int(len(str)/2)
    str = str[:l]
    l = len(str)
    b = ''
    for i in range(0,l,2):
        b += str[i]
    print(b)

no_of_lines = int(input())
store_inp = []

for i in range(no_of_lines):
    store_inp.append(input())

for i in range(no_of_lines):
    first_half(store_inp[i])