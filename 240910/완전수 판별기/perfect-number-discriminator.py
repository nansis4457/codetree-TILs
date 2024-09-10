n = int(input())

c = 0

for i in range(1,n):
    if n % i == 0:
        c += i
    i += 1

if c == n:
    print('P')
else:
    print('N')