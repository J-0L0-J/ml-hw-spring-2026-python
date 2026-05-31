import numpy as np
from sklearn.metrics import precision_score, recall_score

# Input: N
while True:
    try:
        N = int(input("Enter N (number of data points, positive integer): "))
        if N > 0:
            break
        print("N must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Initialize arrays using numpy
y_true = np.empty(N, dtype=int)  # ground truth labels (x values)
y_pred = np.empty(N, dtype=int)  # predicted labels   (y values)

# Input: N (x, y) points
print(f"\nEnter {N} data points. For each point, provide x (true label) then y (predicted label).")
print("Both x and y must be 0 or 1.")
for i in range(N):
    # x = ground truth
    while True:
        try:
            x_val = int(input(f"  Point {i + 1} - x (true label, 0 or 1): "))
            if x_val in (0, 1):
                break
            print("  Value must be 0 or 1. Please try again.")
        except ValueError:
            print("  Invalid input. Please enter 0 or 1.")

    # y = predicted
    while True:
        try:
            y_val = int(input(f"  Point {i + 1} - y (predicted label, 0 or 1): "))
            if y_val in (0, 1):
                break
            print("  Value must be 0 or 1. Please try again.")
        except ValueError:
            print("  Invalid input. Please enter 0 or 1.")

    # Insert into NumPy arrays
    y_true[i] = x_val
    y_pred[i] = y_val

# Compute Precision and Recall
precision = precision_score(y_true, y_pred, zero_division=0)
recall    = recall_score(y_true, y_pred, zero_division=0)

print(f"\nResults:")
print(f"  Precision : {precision:.6f}")
print(f"  Recall    : {recall:.6f}")