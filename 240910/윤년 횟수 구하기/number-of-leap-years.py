n = int(input())
cnt_4 = 0 

for i in range(1,n+1):
    if i % 4 == 0: 
        cnt_4 += 1 
        if i % 100 == 0 and i % 400 != 0:
            cnt_4 -= 1
    i += 1
print(cnt_4)