# a,b = map(int,input().split())

# for i in range(a,b+1):
#     sum_val = 0  
#     cnt = 0 
#     for j in range(1,i):
#         if i % j == 0:
#           sum_val += j
#     if sum_val == i:
#         cnt += 1
# print(cnt) 
# 변수 선언 및 입력:

inp = input()
arr = inp.split()
start, end = int(arr[0]), int(arr[1])
ans = 0

for curr_num in range(start, end + 1):
    # Step 1:
    divisor_sum = 0
    for divisor in range(1, curr_num):
        if curr_num % divisor == 0:
            divisor_sum += divisor

    # Case 1:
    if divisor_sum == curr_num:
        ans += 1

print(ans)