c = 0
cnt = 0
while True:
    n = int(input())
    if n < 30 and n >= 20 :
        c += n
        cnt += 1
        continue
    else:
        break

# cnt가 0이 아닌 경우에만 나눗셈을 수행
if cnt > 0:
    print(f'{c / cnt:.2f}')
else:
    print("입력된 값이 없습니다.")