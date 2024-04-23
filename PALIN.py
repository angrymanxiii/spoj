def is_palindrome(n):
    og = n
    q = 1
    rev = 0
    while q > 0:
        q = n // 10
        r = n % 10
        n = n // 10
        if q >= 0:
            rev = rev * 10 + r
    return rev == og


no_of_lines = int(input())
store_inp = []

for i in range(no_of_lines):
    store_inp.append(int(input()))

for i in range(no_of_lines):
    next_pal = False
    j = store_inp[i] + 1
    while not next_pal:
        next_pal = is_palindrome(j)
        if next_pal:
            print(j)
        j += 1
