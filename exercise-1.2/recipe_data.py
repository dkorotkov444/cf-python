# Step 1: Create an empty Recipe structure to show the expected format
recipe_1 = {
    'name': str(),
    'cooking_time': int(),
    'ingredients': [str()]
}

# Step 2: Create first recipe (Tea)
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"],
}

# Step 3: Create an outer structure and add the first recipe
all_recipes = []
all_recipes.append(recipe_1)

# Step 4: Generate 4 more recipes and add them to the list 
recipe_2 = {
    'name': 'Fried Egg',
    'cooking_time': 3,
    'ingredients': ['Egg', 'Butter', 'Salt', 'Pepper']
}

recipe_3 = {
    'name': 'Guacamole',
    'cooking_time': 0,          # No heat applied
    'ingredients': ['Avocado', 'Lime', 'Onion', 'Cilantro', 'Salt']
}

recipe_4 = {
    'name': 'Pasta Al Dente',
    'cooking_time': 7, 
    'ingredients': ['Pasta', 'Water', 'Salt']
}

recipe_5 = {
    'name': 'Beef Burger',
    'cooking_time': 12,
    'ingredients': ['Ground Beef', 'Burger Bun', 'Lettuce', 'Onion', 'Cheese']
}

all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

# Add aperitivo :-)
recipe_6 = {
    'name': 'Negroni', 
    'cooking_time': 0, 
    'ingredients': ['Gin', 'Sweet Vermouth', 'Campari', 'Orange Peel']
}

all_recipes.append(recipe_6)

# Step 5: Print the ingredients of each recipe
for recipe in all_recipes:
    print(recipe['ingredients'])