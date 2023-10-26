# %%
import random

def get_random_word() -> str:
    '''Returns a random word from the word_list variable.'''
    word_list = ["Banana", "Pineapple", "Orange", "Apple", "Grape"]
    word = random.choice(word_list)
    word = word.lower()
    return word
    
def ask_for_input() -> str:
    '''Requests a single character input from the user. Does not do any validation.'''
    guess = input("Please enter a single letter: \n")
    return guess
    