# n = int(input())
# for i in range(2,n+1):
#     val = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             val += 1
# print(val,end=' ')

# 변수 선언 및 입력
n = int(input())
	
# 1부터 n까지 소수를 구합니다.
for i in range(1, n + 1):
	if i == 1:
		continue
	isprime = True
	for j in range(2, i):
		if i % j == 0:
			isprime = False
	
	if isprime:
		print(i, end=" ")