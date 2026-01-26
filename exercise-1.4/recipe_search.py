# Exercise 1.4 Task

# Import pickle module
import pickle

# Function to display the details of a single recipe
def display_recipe(recipe):
    print(f"Recipe Name: {recipe['name']}")
    print(f"    Cooking Time: {recipe['cooking_time']} minutes")
    print(f"    Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"    Difficulty Level: {recipe['difficulty']}")
    print("-" * 80)

# Function to search for ingredient in the given dictionary
def search_ingredient(data):
    # Retrieve all ingredients from dictionary
    all_ingredients = data.get('all_ingredients', [])

    # Display the complete ingredients list
    print("\nIngredients available across all recipes")
    print("-" * 40)
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")
    print("-" * 40)

    # Prompt user to enter an ingredient to search for
    try:
        search_number = int(input("Enter an ingredient number to search for: "))
        ingredient_searched = all_ingredients[search_number - 1]
        print(f"\nRecipes containing the ingredient: {ingredient_searched}")
        print("-" * 80)
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid ingredient number.") 
        return
    else:
        # Retrieve recipes list from dictionary
        recipes_list = data.get('recipes_list', [])
        found = False
        # Search and display all recipes containing the searched ingredient
        for recipe in recipes_list:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print(f"No recipes found containing the ingredient: {ingredient_searched}")

# Main program execution

try:
    # Prompt user for binary file name
    file_name = str(input("Enter the binary file name to load recipes from: "))
    with open(file_name, 'rb') as recipe_file:
        data = pickle.load(recipe_file)
except (ValueError, FileNotFoundError):
    print("Error loading file. Please ensure the file exists and the name is correct.")
except:
    print("An unknown error occurred while loading the file.")
else:
    search_ingredient(data)
finally:
    print("Recipe search operation completed.")