a,b,c = map(int,input().split(' '))
n = []


if a < b:
    if a < c:
        print('0',end=' ')
    elif a == c:
        print('1',end=' ')
    else:
        print('0',end=' ')

if a == b == c:
    print('1',end=' ')
else:
    print('0',end=' ')