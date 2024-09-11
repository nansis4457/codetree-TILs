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

print(f'{c / cnt:.2f}')