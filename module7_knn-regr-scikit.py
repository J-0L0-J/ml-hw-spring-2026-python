import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Input: N
while True:
    try:
        N = int(input("Enter N (number of data points, positive integer): "))
        if N > 0:
            break
        print("N must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Input: k
while True:
    try:
        k = int(input("Enter k (number of neighbors, positive integer): "))
        if k > 0:
            break
        print("k must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Input: N (x, y) points
X_data = np.empty((N, 1), dtype=float)
y_data = np.empty(N, dtype=float)

print(f"\nEnter {N} data points. For each point, provide x then y:")
for i in range(N):
    while True:
        try:
            x_val = float(input(f"  Point {i + 1} - x: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")
    while True:
        try:
            y_val = float(input(f"  Point {i + 1} - y: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")
    X_data[i, 0] = x_val
    y_data[i] = y_val

# Variance of labels
label_variance = np.var(y_data)
print(f"\nVariance of labels (y values) in training dataset: {label_variance:.6f}")

# Input: query X
while True:
    try:
        X_query = float(input("\nEnter X value to predict Y: "))
        break
    except ValueError:
        print("Invalid input. Please enter a real number.")

# k-NN Regression
if k > N:
    print(f"\nError: k ({k}) must not exceed N ({N}). Cannot perform k-NN regression.")
else:
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_data, y_data)
    X_query_arr = np.array([[X_query]])
    Y_pred = model.predict(X_query_arr)[0]
    print(f"\nk-NN Regression result (k={k}): Y = {Y_pred:.6f}")