# 1.7.1 Practice Script: Setting Up an ORM Model with SQLAlchemy
# This script sets up a simple ORM model for recipes using SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# Create an engine and a base class for declarative class definitions
engine = create_engine("mysql+pymysql://cf-python:75-Graffiti@localhost/recipes_db")
Base = declarative_base()

# Define the Recipe class mapped to the practice_recipes table
class Recipe(Base):
       __tablename__ = "practice_recipes"

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String(50), nullable=False)
       ingredients = Column(String(255))
       cooking_time = Column(Integer)
       difficulty = Column(String(20))

       def __repr__(self):
           return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

# Create the practice_recipes table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new Recipe object and add it to the session
tea = Recipe(
        name = "Tea",
        cooking_time = 5,
        ingredients = "Tea Leaves, Water, Sugar"
    )
session.add(tea)

# Add more recipes to the practice_recipes table
coffee = Recipe(
        name = "Coffee",
        cooking_time = 5,
        ingredients = "Coffee Powder, Sugar, Water"
    )
session.add(coffee)

cake = Recipe(
        name = "Cake",
        cooking_time = 50,
        ingredients = "Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk"
    )
session.add(cake)

banana_smoothie = Recipe(
        name = "Banana Smoothie",
        cooking_time = 5,
        ingredients = "Bananas, Milk, Peanut Butter, Sugar, Ice Cubes"
    )
session.add(banana_smoothie)

# Commit all the added recipes to the database in one go
session.commit()

# Query all recipes from the practice_recipes table
recipes_list = session.query(Recipe).all()

for recipe in recipes_list:
    print("Recipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time)