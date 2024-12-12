0x0A. Prime Game
Project Overview

In this project, you'll apply your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The task involves determining the winner of a game where players take turns removing prime numbers and their multiples from a set of consecutive integers.
Project Details

    Weight: 1
    Project Start: Dec 9, 2024, 6:00 AM
    Project Deadline: Dec 13, 2024, 6:00 AM
    Checker Released: Dec 10, 2024, 6:00 AM
    Auto Review: Launched at the deadline

Problem Statement

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player who cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Maria always goes first, and both players play optimally. The goal is to determine who the winner of each game is, based on the number of rounds won.
Function Prototype
def isWinner(x, nums)

    x: The number of rounds played.
    nums: A list of integers where each element represents the value of n for each round.

Return Value

    Return the name of the player who won the most rounds.
    If there is no winner (i.e., both players won the same number of rounds), return None.

Constraints

    You cannot import any packages.
    n and x will not exceed 10,000.

Example
x = 3
nums = [4, 5, 1]

First round (n = 4):

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because Maria has no prime numbers left to pick.

Second round (n = 5):

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because Ben has no prime numbers left to pick.

Third round (n = 1):

    Ben wins because there are no prime numbers for Maria to pick.

Final result: Ben has the most wins.
Example Usage
isWinner(5, [2, 5, 1, 4, 3])
# Output: 'Ben'

Concepts and Resources
Key Concepts

    Prime Numbers: Understanding prime numbers and how to efficiently find primes within a given range.
    Sieve of Eratosthenes: A highly efficient algorithm for finding all prime numbers up to a given limit.
    Game Theory: Basic principles of competitive games, optimal play, and win conditions.
    Dynamic Programming/Memoization: Techniques for optimizing the solution through reuse of previous results.
    Python Programming: Loops, conditional statements, lists, and arrays to manage game state and track moves.

Recommended Resources

    Khan Academy: Prime Numbers
    Sieve of Eratosthenes in Python
    Game Theory Introduction
    Dynamic Programming with Python Examples
    Python Lists Documentation

Requirements

    Allowed editors: vi, vim, emacs
    All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
    The first line of all files should be #!/usr/bin/python3
    Files must end with a new line
    Code should follow PEP 8 style guide (version 1.7.x)
    All files must be executable

Tasks
0. Prime Game (Mandatory)

Implement the function isWinner(x, nums) to determine the winner of each round and return the player with the most wins.
Repo Structure

    GitHub Repository: alx-interview
    Directory: 0x0A-primegame
    Main File: 0-prime_game.py
