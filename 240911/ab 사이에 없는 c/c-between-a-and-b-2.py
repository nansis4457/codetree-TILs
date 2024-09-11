a, b, c = map(int, input().split())

morphy = True  # Assume all numbers are divisible initially
for i in range(a, b + 1):
    if i % c != 0:
        morphy = False
        break  # Break the loop as soon as a number is not divisible by c

if morphy:
    print("NO")  # All numbers in the range are divisible by c
else:
    print("YES")