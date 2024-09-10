n = int(input())

m = 0
count = 0
for i in range(n):
    i = int(input())
    m += i 
    count += 1
print(f'{m} {m / count:.1f}')