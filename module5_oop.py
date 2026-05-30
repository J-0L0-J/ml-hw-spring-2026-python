class NumberCollection:
    """Handles initialization, insertion, and search of a number collection."""
 
    def __init__(self):
        """Initialize an empty collection."""
        self.numbers = []
 
    def insert(self, number):
        """Insert a number into the collection."""
        self.numbers.append(number)
 
    def search(self, x):
        """
        Search for x in the collection. Returns its 1-based index if found, or -1 if not found.
        """
        for index, num in enumerate(self.numbers, start=1):
            if num == x:
                return index
        return -1
 
 
def main():
    collection = NumberCollection()
 
    # Read N
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            print("N must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
 
    # Read N numbers
    print(f"Enter {n} numbers one by one:")
    for i in range(1, n + 1):
        while True:
            try:
                num = int(input(f"  Number {i}: "))
                collection.insert(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
 
    # Read X and search
    while True:
        try:
            x = int(input("Enter X to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
 
    print(collection.search(x))
 
 
if __name__ == "__main__":
    main()