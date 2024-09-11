s = True

for i in range(5):
    k = int(input())
    if k % 3 == 0:
        s = True
    else:
        s = False

if s == True:
    print('1')
else:
    print('0')