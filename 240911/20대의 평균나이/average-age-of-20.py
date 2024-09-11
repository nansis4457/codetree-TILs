c = 0
cnt = 0
while True:
    n = int(input())
    if n < 30:
        c += n
        cnt += 1
        continue
    else:
        break

# cnt가 0이 아닌 경우에만 평균을 출력
if cnt > 0:
    print(f'{c / cnt:.2f}')
else:
    print("입력된 숫자가 없습니다.")