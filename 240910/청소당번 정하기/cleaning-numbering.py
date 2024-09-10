cnt1 = 0 
cnt2 = 0 
cnt3 = 0 

n = int(input())

for i in range(1,n):
    if i % 2 == 0 and i != 0 :
        cnt1 += 1
    if i % 3 == 0 and i != 0 :
        cnt2 += 1
    if i % 12 == 0 and i != 0 :
        cnt3 += 1

print(cnt1, cnt2, cnt3)