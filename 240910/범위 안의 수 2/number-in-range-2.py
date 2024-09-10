c = 0
count = 0
for i in range(10):
    i = int(input())
    if i >= 0 and i <= 200:
        c += i 
        count += 1
print(f'{c} {c / count:.1f}')