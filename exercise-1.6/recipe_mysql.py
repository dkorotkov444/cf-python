# Exercise 1.6 Task
# This program extends the Recipe class to include MySQL database integration.
# It allows saving and retrieving recipes from a MySQL database.

import mysql.connector
from mysql.connector import Error

# Initialize a connection to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    password='75-Graffiti')

# Initialize a cursor object to interact with the database
cursor = conn.cursor()

# Create the database if it doesn't exist and use it
cursor.execute("CREATE DATABASE IF NOT EXISTS recipes_db")
cursor.execute("USE recipes_db")

# Create the recipes table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
""")

# Function definitions for database operations
# Create, Read, Update, Delete (CRUD) operations

# Function to create and store a new recipe in the database
def create_recipe(conn, cursor):
    try:
        name = input("Enter the recipe name: ")
        cooking_time = int(input("Enter the cooking time (in minutes): "))
        ingredients = []
        print("Enter the ingredient list divided by commas.")
        ingredients_input = input("Ingredients: ")
        ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return None

    # Check for duplicate recipe names
    cursor.execute("SELECT id, name FROM recipes WHERE name=%s", (name,))
    if cursor.fetchone():
        print(f"A recipe with the name '{name}' already exists. Please choose a different name.")
        return None
    
    # Calculate recipe difficulty based on cooking time and number of ingredients
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Insert the new recipe into the database
    ingredients_string = ', '.join(ingredients)
    cursor.execute("""
        INSERT INTO recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    """, (name, ingredients_string, cooking_time, difficulty))
    conn.commit()
    print(f"Recipe '{name}' added successfully!")
    
# Function to calculate recipe difficulty based on cooking time and number of ingredients
# Returns difficulty level as a string
def calculate_difficulty(time, ingredients):
    num_ingredients = len(ingredients)
    if time < 10:                   # Cooking time less than 10 minutes
        difficulty = 'Easy' if num_ingredients < 4 else 'Medium'
    else:                           # Cooking time 10 minutes or more
        difficulty = 'Intermediate' if num_ingredients < 4 else 'Hard'
    return difficulty

# Function to display the details of a single recipe
def display_recipe(name, ingredients, cooking_time, difficulty):
    # Variable ingredients is a string here
    print(f"Recipe Name: {name}")
    print(f"    Cooking Time: {cooking_time} minutes")
    print(f"    Ingredients: {ingredients}")
    print(f"    Difficulty Level: {difficulty}")
    print("-" * 80)

# Function to display a list of all recipes in the database
def display_recipes_list(conn, cursor):
    # Fetch all recipes from the database (difficulty column is not required)
    cursor.execute("SELECT id, name FROM recipes")
    results = cursor.fetchall()
    # Display recipes list
    if results:
        print("\nAll Recipes:" + "\n" + "-"*60)
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]}")
    else:
        print("No recipes found in the database.")

# Function to search for a recipe by ingredient
def search_recipe(conn, cursor):
    all_ingredients = []  # Contains all unique ingredients from the database

    # Fetch all ingredients from the database
    cursor.execute("SELECT ingredients FROM recipes")
    results = cursor.fetchall()
    # Check if there are any recipes in the database
    if not results:
        print("No recipes found in the database.")
        return
    
    # Build the set of all unique ingredients
    for row in results:
        ingredients = row[0].split(', ')
        for ingredient in ingredients:
            ingredient = ingredient.strip().lower()
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Display ingredient search menu
    print("Available ingredients to search for:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")
    
    try:
        # Prompt user to enter an ingredient to search for
        search_number = int(input("Enter an ingredient number to search for: ").strip())
        search_ingredient = all_ingredients[int(search_number)-1]
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid ingredient number.") 
        return
    else:
        print(f"\nRecipes containing the ingredient: {search_ingredient}")
        print("-" * 80)
        # Retrieve relevant recipes from database
        cursor.execute("SELECT * FROM recipes WHERE ingredients LIKE %s", (f"%{search_ingredient}%",))
        results = cursor.fetchall()
        # Display all recipes containing the searched ingredient
        if results:
            for row in results:
                display_recipe(row[1], row[2], row[3], row[4])
        else:
            print(f"No recipes found containing '{search_ingredient}'.")

# Function to update an existing recipe in the database
def update_recipe(conn, cursor):
    # Display a list of all recipes from the database
    display_recipes_list(conn, cursor)

    try:
        recipe_id = int(input("\nEnter the recipe ID to update: ").strip())     # Prompt user to select a recipe to update
        
        # Fetch current record to ensure ID exists and to get current values
        cursor.execute("SELECT name, ingredients, cooking_time FROM recipes WHERE id=%s", (recipe_id,))
        current_recipe = cursor.fetchone()
        
        if not current_recipe:
            print("Recipe not found. Please enter a valid recipe ID.")
            return

        # Initialize variables for SQL query construction
        update_fields = []
        params = []

        # Unpack current values
        name, ingredients_str, cooking_time = current_recipe
        new_name, new_ingredients_str, new_cooking_time = name, ingredients_str, cooking_time
        
        # Prompt user for columns to update
        need_recalc = False
        print(f'''Which columns would you like to update?
        You can update one or several columns:
            (1) Name: {name}
            (2) Ingredients: {ingredients_str}
            (3) Cooking time: {cooking_time}
        If you change the number of ingredients or cooking time, 
        the difficulty will be updated automatically.''')
        columns_input = input("Selection (example: 1,3): ").strip()
        columns_to_update = [col.strip() for col in columns_input.split(',')]

        # Update local variables based on choice
        if '1' in columns_to_update:
            new_name = input("Enter new name: ").strip()
            update_fields.append("name = %s")
            params.append(new_name)
        if '2' in columns_to_update:
            raw_ing = input("Enter new ingredients (comma-separated): ").strip()
            new_ingredients_str = ", ".join([i.strip().lower() for i in raw_ing.split(',')])
            update_fields.append("ingredients = %s")
            params.append(new_ingredients_str)
            need_recalc = len(new_ingredients_str.split(', ')) != len(ingredients_str.split(', '))
        if '3' in columns_to_update:
            new_cooking_time = int(input("Enter new cooking time (in minutes): ").strip())
            update_fields.append("cooking_time = %s")
            params.append(new_cooking_time)
            need_recalc = new_cooking_time != cooking_time

        # Recalculate difficulty in case of changes
        if need_recalc:
            # Note: Split string back to list for the calculation function
            new_difficulty = calculate_difficulty(new_cooking_time, new_ingredients_str.split(', '))
            update_fields.append("difficulty = %s")
            params.append(new_difficulty)

        # Single database Operation
        sql = f"""
            UPDATE recipes 
            SET {', '.join(update_fields)} 
            WHERE id = %s
        """
        cursor.execute(sql, (*params, recipe_id))
        conn.commit()
        print(f"Recipe ID '{recipe_id}' updated successfully!")

    except ValueError:
        print("Invalid input. Numeric value expected.")

# Function to delete a recipe from the database
def delete_recipe(conn, cursor):
    # Display a list of all recipes from the database
    display_recipes_list(conn, cursor)

    try:
        recipe_id = int(input("\nEnter the recipe ID to delete: ").strip())     # Prompt user to select a recipe to delete
        cursor.execute("DELETE FROM recipes WHERE id=%s", (recipe_id,))
    except ValueError:
        print("Invalid input. Numeric value expected.")
    except mysql.connector.Error as err:
        print(f"Database error occurred: {err}")
    else:
        if cursor.rowcount == 0:    # No rows affected means no such ID
            print(f"No recipe found with ID {recipe_id}. No changes made.")
        else:
            conn.commit()
            print(f"Recipe ID '{recipe_id}' deleted successfully!")

# Main program loop
# Display menu and handle user choices
choice = ''
while choice != 'quit':
    print("\nMain Menu:\n" + "="*60)
    print('''Pick a choice:")
        1. Create a new recipe")
        2. Search for a recipe by ingredient")
        3. Update an existing recipe")
        4. Delete a recipe")
    Type 'quit' to exit the program''')
    print("="*60)
    choice = input("Your choice: ").strip().lower()

    if choice == '1':
        create_recipe(conn, cursor)
    elif choice == '2':
        search_recipe(conn, cursor)
    elif choice == '3':
        update_recipe(conn, cursor)
    elif choice == '4':
        delete_recipe(conn, cursor)
    elif choice == 'quit':
        print("Exiting the program. Goodbye!")
    else:
        print("Wrong choice. Please try again.")

# Close the cursor and connection when done
cursor.close()
conn.close()