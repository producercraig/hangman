# %%
import random

word_list = ["Banana", "Pineapple", "Orange", "Apple", "Grape"]
word = random.choice(word_list)

guess = input("Please enter a single letter: \n")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
