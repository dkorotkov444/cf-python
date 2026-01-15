# Exercise 1.3 Task

recipes_list = []
ingredients_list = []

# Function to take recipe input from user
# Returns a single recipe dictionary
def take_recipe ():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    
    print("Enter the ingredient list divided by commas.")
    ingredients_input = input("Ingredients: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

# Take n recipes from user input
n = int(input("How many recipes would you like to enter? "))
for i in range(n):
    print(f"\nEntering recipe {i+1}:")
    recipe = take_recipe()

    # Update ingredients list
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    # Add recipe to recipes list
    recipes_list.append(recipe)

# Assign difficulty level for each recipe and print recipe details
for recipe in recipes_list:
    time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    
    # Assign difficulty based on cooking time and number of ingredients
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

    print("\nRecipe: ", recipe['name'])
    print("Cooking Time (min): ", recipe['cooking_time'])
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