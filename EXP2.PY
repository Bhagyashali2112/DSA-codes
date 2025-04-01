class SetADT: 
    def __init__(self): 
        self.set_a = set([])  # Set A 
        self.set_b = set([])  # Set B 
 
    # Add an element to a specific set 
    def add_element(self, set_name, ele): 
        if set_name == 'a': 
            self.set_a.add(ele) 
        elif set_name == 'b': 
            self.set_b.add(ele) 
 
    # Remove an element from a specific set 
    def remove_element(self, set_name, ele): 
        if set_name == 'a' and ele in self.set_a: 
            self.set_a.remove(ele) 
        elif set_name == 'b' and ele in self.set_b: 
            self.set_b.remove(ele) 
 
    # Display all elements of a set 
    def display_set(self, set_name): 
        if set_name == 'a': 
            print("Set A: ", self.set_a) 
        elif set_name == 'b': 
            print("Set B: ", self.set_b) 
 
    # Check if an element is present in a set 
    def check_element(self, set_name, ele): 
        if set_name == 'a': 
            return "Element is present" if ele in self.set_a else "Element is not present" 
        elif set_name == 'b': 
            return "Element is present" if ele in self.set_b else "Element is not present" 
 
    # Display the size of both sets 
    def size_set(self): 
        print("Size of Set A:", len(self.set_a)) 
        print("Size of Set B:", len(self.set_b)) 
 
    # Union of Set A and Set B 
    def union_set(self): 
        print("Union:", self.set_a.union(self.set_b)) 
 
    # Difference of Set A and Set B (A - B) 
    def difference_set(self): 
        print("Difference (A - B):", self.set_a.difference(self.set_b)) 
 
    # Intersection of Set A and Set B 
    def intersection_set(self): 
        print("Intersection:", self.set_a.intersection(self.set_b)) 
 
    # Check if Set A is a subset of Set B 
    def subset_set_a(self): 
        print("Is Set A a subset of Set B?", self.set_a.issubset(self.set_b)) 
 
    # Check if Set B is a subset of Set A 
    def subset_set_b(self): 
        print("Is Set B a subset of Set A?", self.set_b.issubset(self.set_a)) 
 
 
# Menu and Main Execution Logic 
def menu(): 
    set_adt = SetADT() 
    while True: 
        print("\n==== MENU ====") 
        print("1. Add element to Set A") 
        print("2. Add element to Set B") 
        print("3. Remove element from Set A") 
        print("4. Remove element from Set B") 
        print("5. Display Set A") 
        print("6. Display Set B") 
        print("7. Display size of both sets") 
        print("8. Union of Set A and Set B") 
        print("9. Difference (Set A - Set B)") 
        print("10. Intersection of Set A and Set B") 
        print("11. Check if element is present in Set A") 
        print("12. Check if element is present in Set B") 
        print("13. Check if Set A is a subset of Set B") 
        print("14. Check if Set B is a subset of Set A") 
        print("15. Exit") 
 
        # Input validation for menu choice 
        try: 
            choice = int(input("Enter your choice: ")) 
        except ValueError: 
            print("Invalid input! Please enter a number.") 
            continue 
         
        if choice == 1: 
            ele = int(input("Enter element to add to Set A: ")) 
            set_adt.add_element('a', ele) 
        elif choice == 2: 
            ele = int(input("Enter element to add to Set B: ")) 
            set_adt.add_element('b', ele) 
        elif choice == 3: 
            ele = int(input("Enter element to remove from Set A: ")) 
            set_adt.remove_element('a', ele) 
        elif choice == 4: 
            ele = int(input("Enter element to remove from Set B: ")) 
            set_adt.remove_element('b', ele) 
        elif choice == 5: 
            set_adt.display_set('a') 
        elif choice == 6: 
            set_adt.display_set('b') 
        elif choice == 7: 
            set_adt.size_set() 
        elif choice == 8: 
            set_adt.union_set() 
        elif choice == 9: 
            set_adt.difference_set() 
        elif choice == 10: 
            set_adt.intersection_set() 
        elif choice == 11: 
            ele = int(input("Enter element to check in Set A: ")) 
            print(set_adt.check_element('a', ele)) 
        elif choice == 12: 
            ele = int(input("Enter element to check in Set B: ")) 
            print(set_adt.check_element('b', ele)) 
        elif choice == 13: 
            set_adt.subset_set_a() 
        elif choice == 14: 
            set_adt.subset_set_b() 
        elif choice == 15: 
            print("Exiting program") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
# Run the menu 
menu() 