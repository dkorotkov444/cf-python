# CF Python Exercises

This repository contains CareerFoundry Python coursework scripts for exercises `1.1` through `1.7`.

## Actual Project Structure

```
cf-python/
├── .gitignore
├── README.md
├── requirements.txt
├── exercise-1.1/
│   ├── add-1.1.py
│   └── requirements-1.1.txt
├── exercise-1.2/
│   └── recipe_data.py
├── exercise-1.3/
│   ├── recipe_input_display.py
│   └── practice-scripts/
├── exercise-1.4/
│   ├── recipe_input.py
│   ├── recipe_search.py
│   ├── data/
│   │   └── cookbook.bin
│   └── practice-scripts/
│       ├── 1.4.1-practice.py
│       ├── 1.4.2-practice.py
│       ├── number_list.txt
│       └── recipe_binary.bin
├── exercise-1.5/
│   ├── recipe_oop.py
│   └── practice-scripts/
├── exercise-1.6/
│   └── recipe_mysql.py
└── exercise-1.7/
    └── orm_practice.py
```

## Prerequisites

- Python 3.x
- Windows PowerShell or Command Prompt
- MySQL server (required for `exercise-1.6` and `exercise-1.7`)

## Setup (Windows)

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install currently used packages:

```powershell
pip install -r requirements.txt
```

Optional (for Exercise 1.1 IPython practice dependencies only):

```powershell
pip install -r exercise-1.1\requirements-1.1.txt
```

If using Command Prompt instead of PowerShell:

```bat
.venv\Scripts\activate.bat
```

## Run Scripts

From repository root:

```powershell
python exercise-1.1\add-1.1.py
python exercise-1.2\recipe_data.py
python exercise-1.3\recipe_input_display.py
python exercise-1.4\recipe_input.py
python exercise-1.4\recipe_search.py
python exercise-1.5\recipe_oop.py
python exercise-1.6\recipe_mysql.py
python exercise-1.7\orm_practice.py
```

## Exercise Summary

- **1.1 (`add-1.1.py`)**: Prompts for two integers and prints their sum.
- **1.2 (`recipe_data.py`)**: Builds a list of recipe dictionaries and prints each recipe's ingredient list.
- **1.3 (`recipe_input_display.py`)**: Collects `n` recipes from user input, calculates difficulty, and prints recipes plus a deduplicated ingredient index.
- **1.3 practice scripts**: Basic arithmetic/conditionals, loops, nested conditionals, and string capitalization exercises.
- **1.4 (`recipe_input.py`)**: Loads or initializes pickled recipe data, accepts new recipes, and writes updated data back to a binary file.
- **1.4 (`recipe_search.py`)**: Loads pickled recipe data and searches recipes by selected ingredient.
- **1.4 practice scripts**: Text-file number generation and pickle serialization/deserialization examples.
- **1.5 (`recipe_oop.py`)**: Defines a `Recipe` class with difficulty logic, ingredient search, and demonstration flow.
- **1.5 practice scripts**: `ShoppingList` class methods and a `Height` class with arithmetic/comparison operator overloading.
- **1.6 (`recipe_mysql.py`)**: Console CRUD app for recipes stored in MySQL (`recipes_db.recipes`).
- **1.7 (`orm_practice.py`)**: SQLAlchemy ORM model (`practice_recipes`) and sample inserts/queries against MySQL.

## Data & Database Notes

- `exercise-1.4/data/cookbook.bin` is a generated pickle data file used by the recipe file-storage workflow.
- `exercise-1.6/recipe_mysql.py` and `exercise-1.7/orm_practice.py` use MySQL credentials currently hardcoded as:
	- user: `cf-python`
	- password: `75-Graffiti`
	- host: `localhost`
	- database: `recipes_db`
- Ensure this MySQL user exists and has permissions to create/use `recipes_db` and tables.

## Requirements Files

- Root `requirements.txt` contains current project Python/Django dependencies (Django, pandas, matplotlib, gunicorn, whitenoise, and related packages).
- `exercise-1.1/requirements-1.1.txt` contains IPython shell/practice-specific packages used in early exercise work.

## License

This project is provided for educational purposes.
