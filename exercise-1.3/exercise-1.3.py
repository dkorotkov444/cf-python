# Exercise 1.3 Task
# Create a program that takes n recipes as input from the user.
# Each recipe should include the name, cooking time (in minutes), and a list of ingredients
# The program should calculate the difficulty level of each recipe based on the following criteria:
# - Easy: Cooking time < 10 minutes and number of ingredients < 4
# - Medium: Cooking time < 10 minutes and number of ingredients >= 4
# - Intermediate: Cooking time >= 10 minutes and number of ingredients < 4
# - Hard: Cooking time >= 10 minutes and number of ingredients >= 4
# Finally, the program should print out the details of each recipe along with its difficulty level

recipes_list = []           # Define recipes list to store multiple recipes
ingredients_list = set()    # Define ingredients list as a set to avoid duplicates

# Function to take recipe input from user
# Returns a single recipe dictionary
def take_recipe ():
#    try:
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    
    print("Enter the ingredient list divided by commas.")
    ingredients_input = input("Ingredients: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
#    except ValueError:
#        print("Invalid input. Please enter the correct data types.")
#        return None

    # Create recipe as a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': None
    }
    
    return recipe

# Function to calculate recipe difficulty based on cooking time and number of ingredients
def calculate_difficulty(time, num_ingredients):
    if time < 10:                   # Cooking time less than 10 minutes
        if num_ingredients < 4:     # Less than 4 ingredients
            difficulty = "Easy"
        else:                       # 4 or more ingredients
            difficulty = "Medium"
    else:                           # Cooking time 10 minutes or more
        if num_ingredients < 4:     # Less than 4 ingredients
            difficulty = "Intermediate"
        else:                       # 4 or more ingredients
            difficulty = "Hard"

    return difficulty
    
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
        ingredients_list.add(ingredient)
    
    # Add recipe to recipes list
    recipes_list.append(recipe)

# Assign difficulty level for each recipe and print recipe details
for recipe in recipes_list:
    time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    difficulty = calculate_difficulty(time, num_ingredients)   
    recipe['difficulty'] = difficulty         # Update difficulty in recipe dictionary

    # Print recipe details
    print("\nRecipe: ", recipe['name'])
    print("Cooking Time (min): ", time)
    print("Ingredients:")
    # Nested loop to print ingredients line by line
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty Level: ", difficulty)

# Print the complete ingredients list
print("\nIngredients available across all recipes")
print("-" * 40)
for ingredient in sorted(ingredients_list):
    print(ingredient)