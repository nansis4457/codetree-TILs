cnt = 1 
n = int(input())

for i in range(n):
    for j in range(n):
        print(cnt,end='')
        if cnt <= 8:
            cnt += 1
        else:
            cnt = 1  
    print()