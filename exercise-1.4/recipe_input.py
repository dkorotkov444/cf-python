# Exercise 1.4 Task
# This program takes n recipes as input from the user and stores them in a list.
# For each recipe the user should enter the name, cooking time (in minutes), and a list of ingredients.
# The program calculates the difficulty level of each recipe based on cooking time and number of ingredients.
# Finally, the program stores all details of each recipe into a binary file.
# The script can be run again later to add more recipes.

# Import pickle module for potential future use
import pickle

recipes_list = []               # Define recipes list to store multiple recipes
all_ingredients = []            # Define ingredients list to store all ingredients
ingredients_set = set()     # Define ingredients set to avoid duplicates
# Define data dictionary to store recipes and ingredients
                  

# Function to take recipe input from user
# Returns a single recipe dictionary
def take_recipe():
    try:
        name = input("Enter the recipe name: ")
        cooking_time = int(input("Enter the cooking time (in minutes): "))
        ingredients = []
        print("Enter the ingredient list divided by commas.")
        ingredients_input = input("Ingredients: ")
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return None

    # Calculate recipe difficulty based on cooking time and number of ingredients
    difficulty = calc_difficulty(cooking_time, len(ingredients))

    # Create recipe as a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe

# Function to calculate recipe difficulty based on cooking time and number of ingredients
# Returns difficulty level as a string
def calc_difficulty(time, num_ingredients):
    if time < 10:                   # Cooking time less than 10 minutes
        if num_ingredients < 4:     # Less than 4 ingredients
            difficulty = 'Easy'
        else:                       # 4 or more ingredients
            difficulty = 'Medium'
    else:                           # Cooking time 10 minutes or more
        if num_ingredients < 4:     # Less than 4 ingredients
            difficulty = 'Intermediate'
        else:                       # 4 or more ingredients
            difficulty = 'Hard'

    return difficulty
    
# Open existing binary file to load previous recipes (if any)
try:
    # Prompt user for binary file name
    file_name = str(input("Enter the binary file name to load recipes from: "))
    recipe_file = open(file_name,'rb')    # Attempt to open the binary file in read-binary mode
    data = pickle.load(recipe_file)       # Load data from binary file into dictionary
except ValueError:
    print("File name or path are not in valid format.")
except FileNotFoundError:
    print(f"No binary file named {file_name} found. A new file will be created.")
    # Initialize empty dictionary if file not found
    data = {
        'recipes_list': [],                
        'all_ingredients': []
    }
except:
    print("An unknown error occurred while loading the file. A new file will be created.")
    # Initialize empty dictionary if file not found
    data = {
        'recipes_list': [],                
        'all_ingredients': []
    }
else:
    # Close the file if opened successfully
    recipe_file.close()
    print(f"Loaded {len(data['recipes_list'])} recipes from {file_name}.")
finally:
    # Update recipes_list and all_ingredients_set from data dictionary
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])
    ingredients_set = set(all_ingredients)      # Convert list to set to maintain uniqueness

# Take n recipes from user input
n = int(input("How many recipes would you like to enter? "))
for i in range(n):
    print(f"\nEntering recipe {i+1}:")
    recipe = take_recipe()
    if recipe is None:
        print("Skipping this recipe due to invalid input.")
        continue
    # Update ingredients list
    for ingredient in recipe['ingredients']:
        ingredients_set.add(ingredient)
    # Add recipe to recipes list
    recipes_list.append(recipe)

# Define data dictionary to store updated recipes and ingredients
all_ingredients = list(ingredients_set)    # Convert set back to list for storage
data = {
    'recipes_list': recipes_list,     
    'all_ingredients': all_ingredients    
}

# Store updated recipes and ingredients back into binary file
with open(file_name, 'wb') as file:
    pickle.dump(data, file)