a,b,c = map(int,input().split())
list = []
list.append(a,b,c)
list.sort()
n = len(list)

 if n % 2 == 1:
        median = list[n // 2]
        print(median)
else:
    middle1 = list[n // 2 - 1]
    middle2 = list[n // 2]
    median = (middle1 + middle2) / 2
    print(median)