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