n = int(input())
for i in range(1, n+1): 
    for j in range(1, n-i+2):
        if j == n-i+1:  # 마지막 항목일 때 줄 바꿈
            print(f"{i} * {j} = {i * j}", end='\n')
        else:  # 중간 항목일 때는 ' / '로 구분
            print(f"{i} * {j} = {i * j}", end=" / ")