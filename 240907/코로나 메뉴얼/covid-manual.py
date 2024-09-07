a_1,a_2 = input().split()
b_1,b_2 = input().split()
c_1,c_2 = input().split()

a_2,b_2,c_2 = int(a_2),int(b_2),int(c_2)
A = '' 
B = ''
C = ''

if a_1 == 'Y':
    if a_2 >= 37:
        A = 'A'
    else:
        A = 'C'
elif a_2 >= 37:
        A = 'B'
else:
    A = 'D'

if b_1 == 'Y':
    if b_2 >= 37:
        B = 'A'
    else:
        B = 'C'
elif b_2 >= 37:
    B = 'B'
else:
    B = 'D'

if c_1 == 'Y':
    if c_2 >= 37:
        C = 'A'
    else:
        C = 'C'
elif c_2 >= 37:
    C = 'B'
else:
    C = 'D'


if A == 'A' and ((B == 'A' or C == 'A') or (B == 'A' and C == 'A')):
    print('E')
else:
    print('N')