a,b,c = map(int,input().split())

morphy = True
for i in range(a,b+1):
    if i % c != 0:
        morphy = False

if morphy == False:
    print("YES")
else:
    print("NO")