N = int(input())
# Finding the original number
# keep dividing with the next higher number starting with 2
div = 2
while N > 0:
    N = N // div
    div += 1
N = div - 2
twice = 2*N
# calculating the factorial of 2N
twice_fac = 1
for i in range(1, twice+1):
    twice_fac *= i
# Calculating the number of digits in the factorial of 2N
num_digs_twice_fac = 0
while twice_fac > 0:
    twice_fac = twice_fac // 10
    num_digs_twice_fac += 1

print(N, num_digs_twice_fac)