b, a = map(int,input().split())

k = b
while k >= a and k % 2 == 0:
    print(k,end=' ')
    k += -2