a,b = map(int,input().split())

for i in range(1, 10):
    if i != 0 and i % 2 == 0:
	    for j in range(b, a-1, -1):
			    print(f"{j} * {i} = {i * j}", end="")
			    if j != a:
				    print(" / ", end="");
	    print()