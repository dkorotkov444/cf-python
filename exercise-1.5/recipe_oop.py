# Exercise 1.5 Task
# This program refactors the recipe input program to use Object-Oriented Programming (OOP) principles.
# A Recipe class is created to encapsulate recipe properties and methods.

class Recipe:
    # Class variable to store all unique ingredients across all recipes
    all_ingredients = set()
    # Initialization method for recipe attributes
    def __init__(self, name, cooking_time, ingredients):
        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.difficulty = self.calculate_difficulty()

    # Method to calculate recipe difficulty based on cooking time and number of ingredients
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10:                   # Cooking time less than 10 minutes
            if num_ingredients < 4:                  # Less than 4 ingredients
                return 'Easy'
            else:                                    # 4 or more ingredients
                return 'Medium'
        else:                                        # Cooking time 10 minutes or more
            if num_ingredients < 4:                  # Less than 4 ingredients
                return 'Intermediate'
            else:                                    # 4 or more ingredients
                return 'Hard'
    
    # Getter methods to access recipe attributes
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty
    
    # Setter methods to modify recipe attributes
    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()   # Update difficulty when cooking time changes
    
    def add_ingredients(self, *ingredients):    # *args to accept multiple ingredients
        self.ingredients.extend(ingredients)
        self.difficulty = self.calculate_difficulty()   # Update difficulty when ingredients change
        self.update_all_ingredients()

    # Search methods
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients   
    
    # Method to update class variable with new ingredients
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    # String representation of the Recipe object
    def __str__(self):
        return (f"\nRecipe Name: {self.name}\n"
                f"    Cooking Time: {self.cooking_time} minutes\n"
                f"    Ingredients: {', '.join(self.ingredients)}\n"
                f"    Difficulty: {self.difficulty}\n")

# Function to search for recipes containing a specific ingredient
def recipe_search(data, search_term):
    # data: A list containing Recipe objects
    # search_term: The string ingredient we are looking for
    print(f"Searching for recipes containing: {search_term}")
    print("-" * 60)
    for recipe in data:
        # Call the method search_ingredient which belongs to the Recipe class
        if recipe.search_ingredient(search_term):
            print(recipe)   # If found, we print the recipe object, which calls __str__ method

# Main program code

# Create a sample Recipe object and display its details
print("\nStep 1. Creating and displaying sample recipes.\n" + "-"*60)
tea = Recipe("Tea", 5, [])
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)      

# Create and display 'coffee'
coffee = Recipe("Coffee", 5, [])
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

# Create and display 'cake'
cake = Recipe("Cake", 50, [])
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

# Create and display 'banana_smoothie'
banana_smoothie = Recipe("Banana Smoothie", 5, [])
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)

# Store all recipes in a list
recipes_list = [tea, coffee, cake, banana_smoothie]
pause_input = input("Press Enter to continue...")  # Pause for user input

print("\nStep 2. Searching for recipes.\n" + "-"*60)
# Search for recipes
recipe_search(recipes_list, "Water") 
pause_input = input("Press Enter to continue...")  # Pause for user input
recipe_search(recipes_list, "Sugar")
pause_input = input("Press Enter to continue...")  # Pause for user input
recipe_search(recipes_list, "Bananas")
