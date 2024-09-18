n = int(input())
arr = [['*' for _ in range(n)] for _ in range(n)]

for i in range(1, n-1):
    for j in range(i, n-1):
        arr[i][j] = ' '

for li in arr:
    print(' '.join(li))