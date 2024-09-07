a,b,c = map(int,input().split(' '))

m = min(a,b,c)

if a == m:
        print('1',end=' ')
else:
    print('0',end=' ')


if a == b == c:
    print('1',end=' ')
else:
    print('0',end=' ')