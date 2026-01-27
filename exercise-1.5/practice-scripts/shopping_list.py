# 1.5.1 Practice Script: CCustom methods
# This script creates a shopping list dictionary and populates it using custom methods.

class ShoppingList:
    # Initialize the shopping list with a name and an empty set of items
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = set()

    # Add methods to manipulate the shopping list
    def add_item(self, item):
        self.shopping_list.add(item)

    def remove_item(self, item):
        self.shopping_list.discard(item)

    def view_list(self):
        print(f"Shopping List: {self.list_name}")
        for item in sorted(self.shopping_list):
            print(f" - {item}")
  
print("=== Shopping List Practice Script ===")
print("\nStep 1: Create a shopping list instance and populate it.")
# Create a shopping list instance
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items to the shopping list 
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")
pet_store_list.view_list()                  # View current list

print("\nStep 2: Remove an item from the shopping list.")
pet_store_list.remove_item("flea collars")  # Remove an item from the list
pet_store_list.view_list()                  # View list after removing an item

print("\nStep 3: Attempt to add a duplicate item.")
pet_store_list.add_item("frisbee")          # Attempt to add a duplicate item
pet_store_list.view_list()                  # View list to confirm no duplicates