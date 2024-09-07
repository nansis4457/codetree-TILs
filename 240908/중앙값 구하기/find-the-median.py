a, b, c = map(int, input().split())
numbers = []  # Avoid using 'list' as a variable name
numbers.extend([a, b, c])  # Use extend to add multiple elements
numbers.sort()  # Sort the list

n = len(numbers)

if n % 2 == 1:
    # If odd, pick the middle element
    median = numbers[n // 2]
    print(median)
else:
    # If even, calculate the average of the two middle elements
    middle1 = numbers[n // 2 - 1]
    middle2 = numbers[n // 2]
    median = (middle1 + middle2) / 2
    print(median)