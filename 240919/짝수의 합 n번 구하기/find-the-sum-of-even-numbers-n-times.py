n = int(input())

for i in range(1,n+1):
    a,b = map(int,input().split())
    val = 0 
    for j in range(a,b+1):
        if j % 2 == 0:
            val += j
    print(val)