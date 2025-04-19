# FDE Technical Screen

This project simulates a robotic sorting function for Thoughtful’s automation factory. It classifies packages based on their volume and mass into the correct handling stack.

---

## Objective

Implement and test a Python function that dispatches packages based on:

- **Volume** and **dimensions**
- **Mass**

---

## Sorting Rules

| Condition                          | Classification |
|-----------------------------------|----------------|
| Volume ≥ 1,000,000 cm³ **OR** any dimension ≥ 150 cm | Bulky          |
| Mass ≥ 20 kg                      | Heavy          |

### Stack Assignment:

- **STANDARD**: Neither bulky nor heavy
- **SPECIAL**: Either bulky or heavy
- **REJECTED**: Both bulky **and** heavy

---

## Function

The main logic is implemented in:

```python
sorter/dispatcher.py
```

```python
def sort(width: int, height: int, length: int, mass: int) -> str
```

Returns one of: `"STANDARD"`, `"SPECIAL"`, or `"REJECTED"`

---

## Running Tests

Tests are located in the `tests/` directory.

### How to Run:

```bash
python -m venv .venv
# (If not already active)
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Run tests
pytest
```

set your PYTHONPATH:

```bash
$env:PYTHONPATH="."   # PowerShell (Windows)
export PYTHONPATH=.   # macOS/Linux
```

---

## Project Structure

```
Assessment/
├── sorter/
│   └── dispatcher.py        # Main sorting logic
├── tests/
│   └── test_dispatcher.py   # Unit tests for the sort function
├── .venv/                   # Virtual environment (not uploaded to repo)
└── README.md                # You are here
```

---

## Tech Stack

- **Python 3.11+**
- **pytest** for testing

---

## Author

Aakash Reddy Nuthalapati  
Thoughtful Robotics Automation Challenge  
April 2025

---

## License

This project is for assessment purposes only.
