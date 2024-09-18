m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0  # 각 입력마다 cnt를 0으로 초기화
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1
    print(cnt)  # cnt 값을 출력