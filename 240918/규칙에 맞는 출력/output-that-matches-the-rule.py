n = int(input())

for i in range(n): 
    for j in range(i+1):
        print(n-i+j, end=' ')
    print()

# for i in range(n): 
#     for j in range(n-i):
#         print(n-i - j, end=" ")
#     print()