a_1,a_2 = input().split()
b_1,b_2 = input().split()

a_1,b_1 = int(a_1),int(b_1)

if (a_1 >= 19 and (a_2 == 'M' or a_2 == 'W')) or  (b_1 >= 19 and (b_2 == 'M' or b_2 == 'W')):
    print('1')
else:
    print('0')