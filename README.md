# CF Python Exercises

This repository contains a set of small Python exercises organized by folders. Each exercise is self-contained and may have its own dependencies.

## Project Structure

```
cf-python/
├── .git/               (Hidden Git metadata)
├── .gitignore          (Git ignore rules)
├── README.md           (This file)
├── exercise-1.1/
│   ├── add-1.1.py
│   ├── requirements.txt
│   └── deliverables/
├── exercise-1.2/
│   ├── recipe_data.py
│   └── deliverables/
├── exercise-1.3/
│   ├── recipe_input_display.py
│   ├── practice-scripts/
│   │   ├── 1.3.1-practice.py
│   │   ├── 1.3.2-practice.py
│   │   ├── 1.3.3-practice.py
│   │   ├── add-1.3.py
│   │   ├── conditional-statement.py
│   │   ├── name_capitalizer.py
│   │   └── nested-statement.py
│   └── deliverables/
├── exercise-1.4/
│   ├── recipe_input.py
│   ├── recipe_search.py
│   ├── practice-scripts/
│   │   ├── 1.4.1-practice.py
│   │   └── 1.4.2-practice.py
│   └── deliverables/
├── exercise-1.5/
│   ├── recipe_oop.py
│   ├── practice-scripts/
│   │   ├── shopping_list.py
│   │   └── height.py
│   └── deliverables/
├── exercise-1.6/
│   ├── recipe_mysql.py
│   └── deliverables/
├── exercise-1.7/
│   ├── recipe_app.py
│   ├── practice-scripts/
│   │   └── orm_practice.py
│   └── deliverables/
```

Each main exercise folder contains the primary script(s) for that exercise. Practice scripts are located in the respective `practice-scripts/` subfolders. Deliverables (screenshots, text answers, and Learning Journal) are stored in each exercise's `deliverables/` folder.

## Prerequisites

- Python 3.x installed on your system
- Windows PowerShell (default on Windows)

## Setup (Windows)

Create and activate a virtual environment, then install any exercise-specific dependencies as needed.

```powershell
# From the repository root
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies for a specific exercise (example: 1.1)
pip install -r exercise-1.1\requirements.txt
```

## Running Exercises

To run any exercise script:

- From PowerShell (in the repository root):
  ```powershell
  python exercise-1.1\add.py
  python exercise-1.2\recipe_data.py
  # ...and so on for other exercises
  ```

- From an IPython shell (in the repository root):
  ```powershell
  ipython
  ```
  Then at the IPython prompt:
  ```python
  %run exercise-1.2/recipe_data.py
  # ...and so on for other exercises
  ```

After running a script in IPython, you can interact with its variables and functions.

## Notes

- Each exercise may include its own `requirements.txt`. Install dependencies per exercise as needed.
- If you prefer `cmd` instead of PowerShell, activate the venv using `\.venv\Scripts\activate.bat`.
- Each exercise folder contains deliverables/ sub-folder for non-code exercise work - texts, screenchots, etc.

## Exercise 1.2 Creating recipe data structures

### Data types selection
1. Single recipe: dictionary.
A dictionary optimally represents individual recipes because it allows for a labeled, key-value structure. This provides semantic clarity, making it easy to access particular attributes like "cooking_time" or "ingredients" by name rather than by index in a sequence. It also offers the flexibility to add new attributes or change existing as dictionary is mutable.

2. All recipes outer structure: list.
The list is the most suitable outer structure because it is an ordered, mutable sequence. This allows recipes to be stored in the order they were added and provides the ability to easily sort, append, remove, or modify the collection. Furthermore, a list is highly efficient for iterating through the entire collection to perform mass operations, such as printing every recipe’s ingredients.

## Exercise 1.1 Addition script
This exercise introduces basic Python syntax and arithmetic operations. You will write a simple script to perform addition and get familiar with running Python scripts. It is a gentle introduction to Python programming for beginners.

## Exercise 1.2 Creating recipe data structures
Focuses on Python data types and structures. You will represent recipes as dictionaries and collections of recipes as lists, learning about mutability, key-value access, and best practices for organizing data in Python.

## Exercise 1.3 Recipe input and display
Practice user input, string formatting, and displaying information. You will write scripts that prompt the user for recipe details, process the input, and display results, reinforcing control flow and input validation concepts.

## Exercise 1.4 Recipe input and search
Learn to input, store, and search recipes by ingredients. This exercise introduces file handling, searching within lists, and basic data persistence, helping you build more interactive and useful scripts.

## Exercise 1.5 Object-oriented recipes
Introduces object-oriented programming (OOP) in Python. You will define a Recipe class, use attributes and methods, and see how OOP helps organize and manage recipe data more effectively.

## Exercise 1.6 Recipes and MySQL
Work with databases in Python by connecting to MySQL. You will learn to store, retrieve, and manage recipes using SQL queries and Python database connectors, gaining experience with persistent data storage.

## Exercise 1.7 Recipe app with SQLAlchemy
Build a full-featured recipe CRUD (Create, Read, Update, Delete) application using SQLAlchemy ORM and MySQL. This exercise covers advanced input validation, update logic, and demonstrates how to structure a real-world Python application with a database backend.

## License

This project is provided for educational purposes.
