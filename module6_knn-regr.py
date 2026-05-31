import numpy as np
 
 
class KNNRegression:
    #k-NN Regression using numpy
 
    def __init__(self, k: int):
        self.k = k
        self.points = None  # shape: (N, 2), columns: [x, y]
 
    def fit(self, points: np.ndarray):
        #Store the training points in N x 2 array
        self.points = points
 
    def predict(self, x: float) -> float:
        
        # Predict y for a given x using k-NN regression. Distances are computed along the x-axis only (1-D regression).
        
        if self.points is None or len(self.points) == 0:
            raise ValueError("No data points available. Call fit() first.")
 
        x_vals = self.points[:, 0]          # all x-coordinates
        distances = np.abs(x_vals - x)      # 1D distances
 
        # Indices of the k nearest neighbours (ascending distance)
        k_indices = np.argsort(distances)[: self.k]
 
        y_vals = self.points[k_indices, 1]  # y-coordinates of neighbours
        return float(np.mean(y_vals))       # mean -- regression estimate
 
 
def get_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value > 0:
                return value
            print("Value must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
 
 
def get_float(prompt: str) -> float:
    # Keep asking until the user enters a real number.
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a real number.")
 
 
def main():
 
    N = get_positive_int("\nEnter N (number of data points): ")
 
    k = get_positive_int("Enter k (number of neighbours):  ")
 
    print(f"\nEnter {N} data point(s).  For each point provide x then y.")
    raw_points = []
    for i in range(1, N + 1):
        print(f"\n  Point {i}/{N}:")
        x = get_float(f"    x: ")
        y = get_float(f"    y: ")
        raw_points.append([x, y])
 
    # Build numpy array and initialise model
    points = np.array(raw_points, dtype=float)  # shape (N, 2)
    model = KNNRegression(k=k)
    model.fit(points)
 
    if k > N:
        print(f"Error: k ({k}) is greater than N ({N}).")
        print("k-NN Regression requires k ≤ N.  Please re-run with a valid k.")
    else:
        X_query = get_float("Enter X to predict Y: ")
        Y_pred = model.predict(X_query)
        print(f"\nk-NN Regression result: Y = {Y_pred:.6f}")

 
if __name__ == "__main__":
    main()