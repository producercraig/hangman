# %%
import random

class Hangman:
    def __init__(self, word_list: list, num_lives = 5):
        self.word_list = word_list
        self.word = self._get_random_word()
        self.word_guessed = ["_" for character in self.word]
        self.num_letters = 0 #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives
        self.list_of_guesses = [] #A list of current guesses
    
    def ask_for_input(self):
        '''Requests a single character input from the user.'''
        while True:
            guess = input("Please enter a single character:")
            if self._validate_guess(guess) == False:
                print("Invalid letter. Please enter a single alphabetical character.") 
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self._check_guess(guess):
                    break
                self.list_of_guesses.append(guess)  
                
    def _get_random_word(self) -> str:
        '''Returns a random word from the word_list variable.'''
        word = random.choice(self.word_list)
        word = word.lower()
        print(word) #for testing
        return word
    

    def _validate_guess(self, guess) -> bool:
        '''Takes an inputted  string and returns True if length is 1 and content is alphabetic.'''
        if len(guess) != 1:
            return False
        elif guess.isalpha() == False:
            return False
        else:
            return True
        
    def _check_guess(self, guess) -> bool:
        '''Takes the validated character and returns True/False depending on if the character is present in the random word.'''
        guess = guess.lower()

        if guess in self.word:
            i = 0
            for character in self.word:
                self.word_guessed[i] = character
            self.num_letters -= 1
            return True
        else:
            self.num_lives -= 1
            print(f"Sorry. {guess} is not in the word.")
            print(f"You have {self.num_lives} left.")
            return False

            
   

                    


    
hangman2 = Hangman(["One", "Two", "Three"], 6)
hangman2.ask_for_input()