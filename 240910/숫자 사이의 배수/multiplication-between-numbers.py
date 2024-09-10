a,b = map(int,input().split())
c_sum = 0
c_mean = 0
count = 0 
for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        c_sum += i
        count += 1 
c_mean = c_sum / count

print(f'{c_sum} {c_mean:.1f}')