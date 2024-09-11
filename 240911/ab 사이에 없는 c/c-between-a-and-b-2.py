a,b,c = map(int,input().split())

morphy = True
for i in range(a,b+1):
    if i % c != 0:
        morphy = False
    else:
        morphy = True

if morphy == False:
    print("YES")
else:
    print("NO")