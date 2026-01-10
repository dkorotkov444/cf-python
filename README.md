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
├── exercise-1.2/       (Future work)
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

- Exercise 1.1 (add two numbers):
   ```powershell
   python exercise-1.1\add.py
   ```

Additional exercises (1.2, 1.3, 1.4) will be run similarly from their respective folders.

## Notes

- Each exercise may include its own `requirements.txt`. Install dependencies per exercise as needed.
- If you prefer `cmd` instead of PowerShell, activate the venv using `\.venv\Scripts\activate.bat`.
- Each exercise folder contains deliverables/ sub-folder for non-code exercise work - texts, screenchots, etc.

## License

This project is provided for educational purposes.
