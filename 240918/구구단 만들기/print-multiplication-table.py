# a,b = map(int,input().split())

# for i in range(b,a,-1):
#     if i % 2 == 0:
#         for j in range(1,10):
#             print(f'{i} * {j} = {i * j}',end=' ')
#             if j < b-1:
#                 print('/',end=' ')
#     print()

arr = input().split()
a, b = int(arr[0]), int(arr[1])

for i in range(1, 10):
# range 조건에 a까지 2씩 차감하는 방식 (a, b는 모두 짝수이므로 2씩 감소해도 짝수)
    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {j * i}", end = "")
        if j > a:
            print(" /", end = " ")
    print()