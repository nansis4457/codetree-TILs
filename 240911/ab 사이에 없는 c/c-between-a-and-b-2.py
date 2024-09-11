a, b, c = map(int, input().split())

morphy = True
for i in range(a, b + 1):
    if i % c != 0:
        morphy = False
        break  # 한 번이라도 나누어 떨어지지 않으면 반복 종료

if morphy == False:
    print("YES")
else:
    print("NO")