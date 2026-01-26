# 1.4.2 Practice: Saving a Recipe with Pickle
# This script creates a dictionary representing a recipe and saves it to a file using the pickle module.

# Import the pickle module
import pickle

# Create a recipe dictionary
recipe = {
    'name': 'Tea', 
    'ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'cooking_time': 5,
    'difficulty': 'Easy'
}

# Save the recipe dictionary to a binary file using pickle
with open('recipe_binary.bin', 'wb') as recipe_file:
    pickle.dump(recipe, recipe_file)

# Load the recipe dictionary back from the binary file to verify
with open('recipe_binary.bin', 'rb') as recipe_file:
    loaded_recipe = pickle.load(recipe_file)
    
# Print the loaded recipe to verify correctness
print(f"Recipe name: {loaded_recipe['name']}")
print(f"    Ingredients: {', '.join(loaded_recipe['ingredients'])}")
print(f"    Cooking time (minutes): {loaded_recipe['cooking_time']}")
print(f"    Difficulty: {loaded_recipe['difficulty']}")