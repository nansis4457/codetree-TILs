a = int(input())


for i in range(1,a+1):
    if i % 2 == 0 and i % 4 != 0:
        continue  
    if i // 8 == 2 or i // 8 == 4 or i // 8 == 6 or i // 8 == 8 or i // 8 == 0:
        continue
    if i % 7 < 4:
        continue
    print(i, end=' ')