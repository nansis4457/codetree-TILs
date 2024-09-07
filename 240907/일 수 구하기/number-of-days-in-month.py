n = int(input())
if n % 2 == 1:
    if 9 <= n < 11:
        print('30')
    else:
        print('31')    
elif n != 2 and (n % 2 == 0):
    if 8 <= n <= 12:
        print('31')
    else:
        print('30')
else:
    print('28')

    #31 ->