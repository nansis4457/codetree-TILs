inp = input()
arr = inp.split()
start, end = int(arr[0]), int(arr[1])
ans = 0
tr = 0
for curr_num in range(start, end + 1):
    # Step 1:
    divisor_sum = 0
    for divisor in range(1, curr_num):
        if curr_num % divisor == 0:
            ans += 1

    # Case 1:
    if ans == 3:
        tr += 1

print(tr)