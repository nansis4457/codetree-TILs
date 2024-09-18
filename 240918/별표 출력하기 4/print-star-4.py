n = int(input())

for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

for i in range(n-2,-1,-1):     #5 -> 2 4->3 
    for j in range(n-i):
        print('*',end=' ')
    print()