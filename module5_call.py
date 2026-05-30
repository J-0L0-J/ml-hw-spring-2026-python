from module5_mod import NumberCollection
 
 
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
                print("  Invalid input. Please enter a valid integer.")
 
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