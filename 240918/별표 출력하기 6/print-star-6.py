n = int(input())

# 위쪽 부분
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(' ', end=' ')
    # 별 출력 (별 사이에는 공백 없이)
    for j in range((2 * n) - (2 * i) - 1):
        print('*', end=' ')
    print()

# 아래쪽 부분
for i in range(n-1):
    # 공백 출력
    for j in range(n - i - 2):
        print(' ', end=' ')
    # 별 출력 (별 사이에는 공백 없이)
    for j in range(3 + (2 * i)):
        print('*', end=' ')
    print()