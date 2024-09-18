n = int(input())

# 위쪽 부분
for i in range(n):
    # 공백 출력
    for j in range(n-i-1):
        print(' ', end='')
    # 별 출력 (별 사이에는 공백 없이)
    for j in range(2*i + 1):
        print('*', end='')
    print()
# 아래쪽 부분
for i in range(n):
    # 공백 출력
    for j in range(i+1):
        print(' ', end='')
    # 별 출력 (별 사이에는 공백 없이)
    for j in range((2 * n) - (2 * i) - 3):
        print('*', end='')
    print()