n = int(input())

for k in range(1, n+1):
    
    if k % 3 == 0:  # k가 3의 배수가 아니면
        print('0', end=' ')
    elif '3' in str(k) or '6' in str(k) or '9' in str(k):  # k에 '3', '6', '9' 중 하나가 포함되면
        print('0', end=' ')
    else:
        print(k, end=' ')
    k += 1