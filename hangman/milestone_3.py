# %%
import milestone_2 as m2

word = m2.get_random_word()
print(word)

def ask_for_input():
    '''Requests a single character input from the user.'''
    while True:
        guess = input("Please enter a single character: \n")
        if validate_guess(guess):
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def validate_guess(guess) -> bool:
    '''Takes an inputted  string and returns True if length is 1 and content is alphabetic.'''
    if len(guess) != 1:
        return False
    elif guess.isalpha() == False:
        return False
    else:
        return True
    
def check_guess(guess) -> bool:
    guess = guess.lower()
    if guess in word:
        print (f"Good guess! {guess} is in the word.")
    else:
        print (f"Sorry, {guess} is not in the word. Try again.")


ask_for_input()
