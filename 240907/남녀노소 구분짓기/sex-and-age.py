a = int(input())
b = int(input())

if a == 1:
    if b >= 19:
        print('WOMAN')
    else:
        print('GIRL')
elif b >= 19:
    print('MAN')
else:
    print('BOY')