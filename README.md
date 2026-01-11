# CF Python Exercises

This repository contains a set of small Python exercises organized by folders. Each exercise is self-contained and may have its own dependencies.

## Project Structure

```
cf-python/ (The Root - Open this in VS Code)
├── .git/               (Hidden Git metadata)
├── .gitignore          (Tells Git to ignore your venv)
├── README.md           (Overview of the course)
├── exercise-1.1/  
│   ├── deliverables/   (Exercise deliverables - texts, screenchots, etc.)
│   ├── add.py
│   └── requirements.txt
├── exercise-1.2/       (Data types in Python)
│   ├── deliverables/   (Exercise deliverables - texts, screenchots, etc.)
│   ├── recipe_data.py
├── exercise-1.3/       (Future work)
└── exercise-1.4/       (Future work)
```

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


## License

This project is provided for educational purposes.
