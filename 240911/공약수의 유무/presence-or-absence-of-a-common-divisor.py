a,b = map(int,input().split())
n1 = 1920 ; n2 = 2880
 
morphy = False
for i in range(a,b+1):
    if n1 % i == 0 and n2 % i == 0:
        morphy = True

if morphy == True:
    print('1')
else:
    print("0")