c = 0
cnt = 0
while True:
    n = int(input())
    if n < 30:
        c += n
        cnt += 1
        continue
    elif n >= 30:
        break

# 루프가 종료된 후 평균값 출력
if cnt > 0:
    print(f'{c / cnt:.2f}')