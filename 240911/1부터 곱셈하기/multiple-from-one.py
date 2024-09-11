n = int(input())
c = 1 
for i in range(1,n+1):
    c *= i
    if c <= n:
        continue
    else:
        break 
print(i)