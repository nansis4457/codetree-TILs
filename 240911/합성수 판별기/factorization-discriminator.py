n = int(input())

morphy = False
for i in range(2,n-1):
    if n % i == 0:
        morphy = True

if morphy == True:
    print("C")
else:
    print("N")