# Hangman

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Installation Instructions](#installation-instructions)
- [How to Play](#how-to-play)
- [Game Componenets](#game-components)
    - [Hangman Class](#hangman-class)
    - [Utility Functions](#utility-functions)
- [File Structure](#file-structure)

## Description

Welcome to the Hangman Game implemented in Python. This game is a text-based version of the classic word-guessing game. The player tries to guess the letters of a hidden word, with a limited number of attempts.

## Requirements
- Python 3.x

## Installation Instructions
- Download or clone the project
- Run milestone_5.py

## How to Play
1. Run the script in a Python environment.
2. You will be presented with a series of underscores representing the hidden word.
3. You are prompted to enter a single letter guess.
4. If the guess is correct, the letter will be revealed in the word.
5. If the guess is incorrect, you lose a life.
6. The game continues until you guess the word or run out of lives.

## Game Components
- Hangman Class
    - Attributes:
        - word_list: A list of possible words for the game.
        - word: The current word to be guessed.
        - word_guessed: A representation of the guessed letters and remaining blanks in the word.
        - num_letters: The number of unique letters in the word.
        - num_lives: The number of wrong guesses allowed (default 5).
        - list_of_guesses: A list of letters guessed so far.
    - Methods:
        - ask_for_input(): Prompts the player for a guess and processes it.
        - get_num_lives(): Returns the current number of lives.
        - display_word_guessed(): Displays the current state of the guessed word.
        - display_word(): Reveals the complete word.

- Utility Functions
    - play_game(word_list): Function to start the game. Takes a list of words as input.
        - Example usage:
          ```python
          play_game(["Python", "Unity", "Unreal", "Programming", "Abstraction", "Testing"])

## File Structure
- hangman
    - hangman_Template.py
    - milestone_2.py // Test file handling random word generation
    - milestone_3.py // Test file handling user input and validation
    - milestone_4.py // Test file containing the previous Hangman class used to run the game
    - milestone_5.py // Contains the Hangman() class and play_game() method required to run the game
- .gitignore
- README.md
