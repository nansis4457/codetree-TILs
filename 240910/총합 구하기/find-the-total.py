a,b = map(int,input().split())

c = 0 
for i in range(a,b+1):
    if i % 6 == 0 and i % 8 != 0:
        c += i 
    i += 1
print(c)