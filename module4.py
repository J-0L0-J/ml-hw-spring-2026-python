# module4.py

# Step 1: Ask for N
N = int(input('Enter a positive integer N: '))

# Step 2: Read N numbers one by one
numbers = []
for i in range(1, N + 1):
    user_num = int(input(f'Enter number {i}: '))
    numbers.append(user_num)

# Step 3: Ask for X and search entire list using a for loop
X = int(input('Please enter the integer X: '))

found = False
for i in range(N):
    if numbers[i] == X:
        print(f"Found at index: {i + 1}")  # convert to 1-based index
        found = True

if not found:
    print(-1)
