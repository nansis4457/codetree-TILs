a,b = map(int,input().split())
c = 0
if a < b:
    for i in range(a,b+1):
        if i % 5 == 0:
            c += i
        i += 1
else: 
    for i in range(b,a+1):
        if i % 5 == 0:
            c += i
        i += 1
print(c)