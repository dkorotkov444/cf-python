# CF Python Exercises

This repository contains CareerFoundry Python coursework artifacts organized by exercise folders.

## Repository Scope

- Includes Python learning exercises (`exercise-1.1` to `exercise-1.7`) with scripts, practice files, and deliverables.
- Includes later coursework folders (`exercise-2.1` to `exercise-2.8`) that currently contain deliverables/artifacts.
- The Bookstore Django application is no longer part of this repository and has been moved to a standalone repository.

## Current Structure (Summary)

```
cf-python/
├── README.md
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
│   └── deliverables/
├── exercise-1.4/
│   ├── recipe_input.py
│   ├── recipe_search.py
│   ├── data/
│   ├── practice-scripts/
│   └── deliverables/
├── exercise-1.5/
│   ├── recipe_oop.py
│   ├── practice-scripts/
│   └── deliverables/
├── exercise-1.6/
│   ├── recipe_mysql.py
│   └── deliverables/
├── exercise-1.7/
│   ├── practice-scripts/
│   └── deliverables/
└── exercise-2.1 ... exercise-2.8/
```

## Prerequisites

- Python 3.x
- Windows PowerShell (or Command Prompt)

## Setup (Windows)

From repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies only where needed (currently required in `exercise-1.1`):

```powershell
pip install -r exercise-1.1\requirements.txt
```

## Running Scripts

Run scripts directly from repository root:

```powershell
python exercise-1.1\add-1.1.py
python exercise-1.2\recipe_data.py
python exercise-1.3\recipe_input_display.py
python exercise-1.4\recipe_input.py
python exercise-1.4\recipe_search.py
python exercise-1.5\recipe_oop.py
python exercise-1.6\recipe_mysql.py
```

Optional (IPython):

```powershell
ipython
```

Then run files with:

```python
%run exercise-1.2/recipe_data.py
```

## Exercise Overview

- **1.1**: Basic Python arithmetic and script execution.
- **1.2**: Python data structures for recipe data.
- **1.3**: User input and formatted output.
- **1.4**: Recipe search and file-based workflow.
- **1.5**: Object-oriented programming with recipe classes.
- **1.6**: MySQL integration from Python.
- **1.7**: ORM practice artifacts and deliverables.
- **2.1–2.8**: Coursework deliverables and supporting artifacts.

## Notes

- Many folders include `deliverables/` for submissions (screenshots, journals, PDFs, and text files).
- If using Command Prompt instead of PowerShell, activate with `.venv\Scripts\activate.bat`.
- For Bookstore app development, use the separate standalone Bookstore repository.

## License

This project is provided for educational purposes.
