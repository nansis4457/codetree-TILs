# n = int(input())
# cnt = 1

# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0:
#             print(cnt, end=" ")
#             cnt += 1  # 들여쓰기 수정
#         else:
#             print(cnt, end=" ")
#             cnt += 2  # 들여쓰기 수정
#     print()  # 줄바꿈을 위해 print()를 추가

n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(j+1+3*i*n//2, end=' ')
        else:
            print(n*((i+(i+1)//2)-1)+(2*j+2), end=' ')
    print()