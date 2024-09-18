# 변수 선언 및 입력
n = int(input())
	
# n칸의 정사각형에 올바른 숫자를 출력합니다.
for i in range(1,n+1):
	for j in range(n,0,-1):
		print(i*j, end=" ")
	print()