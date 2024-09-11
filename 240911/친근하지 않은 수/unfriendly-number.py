n = int(input())
c = 0
for i in range(1,n+1):
    
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    else: 
        c += 1
    i += 1
    

print(c)