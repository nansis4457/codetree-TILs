n = int(input())
cnt = 0
while n != 1:  # n이 1이 될 때까지 반복
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    cnt += 1  # 모든 반복에서 cnt 증가

print(cnt)