# n = int(input())

# for i in range(1, 2*n+1): 
#     if i % 2 == 0:
#         # i // 2로 정수 나눗셈 사용
#         for j in range(1 + (i // 2)):
#             print("*", end=" ")
#         print()
#     else:
#         # (i - 1) // 2로 정수 나눗셈 사용
#         for j in range(n - (i - 1) // 2):
#             print("*", end=" ")
#         print()
n = int(input())

x = 1
y = n

for i in range(2*n):
    if i % 2 != 0:
        for _ in range(y):
            print("*",end=" ")
        print()
        y -= 1
    else:
        for _ in range(x):
            print("*",end=" ")
        print()
        x += 1