a_1,a_2 = map(int,input().split())
b_1,b_2 = map(int,input().split())


if a_2 < b_2:
    print('B')
elif a_1 > b_1:
    print('A')
else:
    print('B')