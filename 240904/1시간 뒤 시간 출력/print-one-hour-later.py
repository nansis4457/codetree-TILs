a = input().split(':')
a = [int(x) for x in a]  # Convert each part to an integer
print(f"{a[0] + 1}:{a[1]}")  # Add 1 to the first part and print