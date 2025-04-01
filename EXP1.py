class HashTable: 
    def __init__(self): 
        self.m = int(input("Enter size of hash table: ")) 
        self.hashTable = [None] * self.m 
        self.elecount = 0 
        print(self.hashTable)  # Prints the initial empty hash table 
 
    # Hash Function 
    def hashFunction(self, key): 
        return key % self.m 
 
    # Check if table is full 
    def is_full(self): 
        return self.elecount == self.m 
 
    # Linear Probing Insert Method 
    def linear_probing_insert(self, key, data): 
        index = self.hashFunction(key) 
        comparisons = 0 
        while self.hashTable[index] is not None: 
            comparisons += 1 
            index = (index + 1) % self.m 
        self.hashTable[index] = [key, data] 
        self.elecount += 1 
        print(f"Data inserted at {index}, Comparisons: {comparisons}") 
        print(self.hashTable) 
 
    # Linear Probing Search Method 
    def get_linear(self, key): 
        index = self.hashFunction(key) 
        comparisons = 0 
        while self.hashTable[index] is not None: 
            comparisons += 1 
            if self.hashTable[index][0] == key: 
                print(f"Found key at index {index}, Comparisons: {comparisons}") 
                return index 
            index = (index + 1) % self.m 
        print("Key not found") 
        return None 
 
    # Quadratic Probing Insert Method 
    def quadratic_probing_insert(self, key, data): 
        index = self.hashFunction(key) 
        comparisons = 0 
        i = 1  # Start with i=1 for quadratic probing 
        while self.hashTable[index] is not None: 
            comparisons += 1 
            index = (index + i * i) % self.m 
            i += 1 
        self.hashTable[index] = [key, data] 
        self.elecount += 1 
        print(f"Data inserted at {index}, Comparisons: {comparisons}") 
        print(self.hashTable) 
 
    # Quadratic Probing Search Method 
    def get_quadratic(self, key): 
        index = self.hashFunction(key) 
        comparisons = 0 
        i = 0  # Start with i=0 for quadratic probing 
        while self.hashTable[index] is not None: 
            comparisons += 1 
            if self.hashTable[index][0] == key: 
                print(f"Found key at index {index}, Comparisons: {comparisons}") 
                return index 
            i += 1 
            index = (index + i * i) % self.m 
        print("Key not found") 
        return None 
 
    # Insert using Linear Probing 
    def insert_via_linear(self, key, data): 
        if self.is_full(): 
            print("Table is full") 
            return False 
        index = self.hashFunction(key) 
        if self.hashTable[index] is None: 
            self.hashTable[index] = [key, data] 
            self.elecount += 1 
            print(f"Data inserted at {index}") 
            print(self.hashTable) 
        else: 
            print("Collision occurred, applying linear probing.") 
            self.linear_probing_insert(key, data) 
 
    # Insert using Quadratic Probing 
    def insert_via_quadratic(self, key, data): 
        if self.is_full(): 
            print("Table is full") 
            return False 
        index = self.hashFunction(key) 
        if self.hashTable[index] is None: 
            self.hashTable[index] = [key, data] 
            self.elecount += 1 
            print(f"Data inserted at {index}") 
            print(self.hashTable) 
        else: 
            print("Collision occurred, applying quadratic probing.") 
            self.quadratic_probing_insert(key, data) 
 
# Menu and Main Execution Logic 
def menu(): 
    obj = HashTable() 
    while True: 
        print("********") 
        print("1. Linear Probe Insert/Search") 
        print("2. Quadratic Probe Insert/Search") 
        print("3. Exit") 
        print("********") 
        choice = int(input("Enter choice: ")) 
        if choice == 1: 
            while True: 
                print("1. Insert") 
                print("2. Search") 
                print("3. Exit") 
                sub_choice = int(input("Enter your choice: ")) 
                if sub_choice == 1: 
                    key = int(input("Enter phone number (key): ")) 
                    name = input("Enter name: ") 
                    obj.insert_via_linear(key, name) 
                elif sub_choice == 2: 
                    key = int(input("Enter phone number (key) to search: ")) 
                    obj.get_linear(key) 
                elif sub_choice == 3: 
                    break 
        elif choice == 2: 
            while True: 
                print("1. Insert") 
                print("2. Search") 
                print("3. Exit") 
                sub_choice = int(input("Enter your choice: ")) 
                if sub_choice == 1: 
                    key = int(input("Enter phone number (key): ")) 
                    name = input("Enter name: ") 
                    obj.insert_via_quadratic(key, name) 
                elif sub_choice == 2: 
                    key = int(input("Enter phone number (key) to search: ")) 
                    obj.get_quadratic(key) 
                elif sub_choice == 3: 
                    break 
        elif choice == 3: 
            break 
 
# Run the menu 
menu() 