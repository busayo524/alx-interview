# 0x08. Making Change

## Algorithm | Python

This project tackles the **coin change problem**, a classic algorithmic challenge involving **dynamic programming** and **greedy algorithms**. The goal is to determine the minimum number of coins required to achieve a given amount using available denominations.

---

## Table of Contents
- [Concepts](#concepts)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Resources](#resources)
- [Usage](#usage)

---

## Concepts

### Greedy Algorithms
- **How it works**: Select the largest denomination coin until the amount is met.
- **Limitations**: Greedy algorithms are efficient but may not always provide optimal solutions for certain denominations.

### Dynamic Programming
- **Core ideas**: 
  - **Overlapping subproblems**: Break the problem into smaller, reusable computations.
  - **Optimal substructure**: The solution to the overall problem depends on solutions to subproblems.
- **Approach**: Iterative or recursive methods to compute the minimum coins.

### Algorithmic Complexity
- Strive for a solution with low time and space complexity to handle large inputs efficiently.

### Problem-Solving Strategies
- Divide the problem into manageable sub-problems.
- Use either iterative loops or recursive techniques based on the situation.

---

## Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Environment**:
  - Ubuntu 20.04 LTS
  - Python 3.4.3
- **File Standards**:
  - All files should end with a new line.
  - First line of all Python files must be: `#!/usr/bin/python3`.
- **Coding Style**: PEP 8 (version 1.7.x).
- **Executability**: All files must be executable.
- **Mandatory Files**:
  - `README.md` at the root of the project folder.

---

## Tasks

### 0. Change comes from within
**Mandatory**

Write a function `makeChange(coins, total)` that determines the minimum number of coins required to meet a given total.

#### Prototype:
```python
def makeChange(coins, total):
Specifications:

    Return:
        Fewest number of coins needed to achieve total.
        0 if total is 0 or less.
        -1 if the total cannot be met using the given coins.
    Input:
        coins: A list of integers representing coin denominations.
        total: An integer representing the target amount.
    Assumptions:
        Coin values are integers greater than 0.
        Infinite supply of each coin.

Example:

makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1

File:

    0-making_change.py

Resources

    Python Documentation:
        Control Flow Tools
    GeeksforGeeks Articles:
        Coin Change | DP-7
        Greedy Algorithm for Minimum Coins
    YouTube Tutorials:
        Dynamic Programming - Coin Change Problem

Usage
Testing the function:

1. Create a 0-main.py file:
#!/usr/bin/python3
"""
Main file for testing
"""
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

2. Run the file:
chmod +x 0-main.py
./0-main.py

Expected Output:
7
-1

# 0x08. Making Change

## Algorithm | Python

This project tackles the **coin change problem**, a classic algorithmic challenge involving **dynamic programming** and **greedy algorithms**. The goal is to determine the minimum number of coins required to achieve a given amount using available denominations.

---

## Table of Contents
- [Concepts](#concepts)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Resources](#resources)
- [Usage](#usage)

---

## Concepts

### Greedy Algorithms
- **How it works**: Select the largest denomination coin until the amount is met.
- **Limitations**: Greedy algorithms are efficient but may not always provide optimal solutions for certain denominations.

### Dynamic Programming
- **Core ideas**: 
  - **Overlapping subproblems**: Break the problem into smaller, reusable computations.
  - **Optimal substructure**: The solution to the overall problem depends on solutions to subproblems.
- **Approach**: Iterative or recursive methods to compute the minimum coins.

### Algorithmic Complexity
- Strive for a solution with low time and space complexity to handle large inputs efficiently.

### Problem-Solving Strategies
- Divide the problem into manageable sub-problems.
- Use either iterative loops or recursive techniques based on the situation.

---

## Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Environment**:
  - Ubuntu 20.04 LTS
  - Python 3.4.3
- **File Standards**:
  - All files should end with a new line.
  - First line of all Python files must be: `#!/usr/bin/python3`.
- **Coding Style**: PEP 8 (version 1.7.x).
- **Executability**: All files must be executable.
- **Mandatory Files**:
  - `README.md` at the root of the project folder.

---

## Tasks

### 0. Change comes from within
**Mandatory**

Write a function `makeChange(coins, total)` that determines the minimum number of coins required to meet a given total.

#### Prototype:
```python
def makeChange(coins, total):

Specifications:

    Return:
        Fewest number of coins needed to achieve total.
        0 if total is 0 or less.
        -1 if the total cannot be met using the given coins.
    Input:
        coins: A list of integers representing coin denominations.
        total: An integer representing the target amount.
    Assumptions:
        Coin values are integers greater than 0.
        Infinite supply of each coin.

Example:

makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1

File:

    0-making_change.py

Resources

    Python Documentation:
        Control Flow Tools
    GeeksforGeeks Articles:
        Coin Change | DP-7
        Greedy Algorithm for Minimum Coins
    YouTube Tutorials:
        Dynamic Programming - Coin Change Problem

Usage
Testing the function:

1. Create a 0-main.py file:

#!/usr/bin/python3
"""
Main file for testing
"""
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

2. Run the file:

    chmod +x 0-main.py
    ./0-main.py

Expected Output:

7
-1

Repository Structure
alx-interview
└── 0x08-making_change
    ├── README.md
    ├── 0-making_change.py
    └── 0-main.py
