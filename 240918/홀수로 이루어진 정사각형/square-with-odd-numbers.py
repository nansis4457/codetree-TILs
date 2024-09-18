# 변수 선언 및 입력
n = int(input())
	
# n칸의 정사각형에 올바른 숫자를 출력합니다.
for i in range(n):
	for j in range(n):
		print(i * 2 + j * 2 + 11, end=" ")
	print()