# %%
import random

class Hangman:
    def __init__(self, word_list: list, num_lives = 5):
        self.word_list = word_list
        self.word = self._get_random_word()
        self.word_guessed = ["_" for character in self.word] #List of underscores representing unguessed characters
        self.num_letters = self._get_unique_letter_count() #The number of UNIQUE letters in the word that have not been guessed yet
        self._num_lives = num_lives #Number of incorrect guesses allowed
        self.list_of_guesses = [] #A list of current guesses

    def ask_for_input(self):
        '''Public method which requests a single character input from the user and calls validate_guess and check_guess if the input is valid.'''
        guess = input("Please enter a single character:")
        if self._validate_guess(guess) == False:
            print("Invalid letter. Please enter a single alphabetical character.") 
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)  
            if self._check_guess(guess):
                print(f"Correct guess! {self.display_word_guessed()}")   

    def get_num_lives(self) -> int:
        '''Public method for getting the number of lives. Prevents external modification.'''
        return self._num_lives
    
    def display_word_guessed(self) -> str:
        word_guessed_string = ""
        for character in self.word_guessed:
            word_guessed_string += (character + " ")
        word_guessed_string = word_guessed_string[0].upper() + word_guessed_string[1:]
        return word_guessed_string
                
    def _get_random_word(self) -> str:
        '''Returns a random word from the word_list variable.'''
        word = random.choice(self.word_list)
        word = word.lower()
        #print(f"[*FOR TESTING PURPOSES*] The word is: {word}") #for testing
        return word
    
    def _get_unique_letter_count(self) -> int:
        unique_set = set(self.word)
        return len(unique_set)

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
            self._update_word_guessed(guess)
            self.num_letters -= 1
            return True
        else:
            self._num_lives -= 1
            print(f"Sorry. {guess} is not in the word.")
            print(f"You have {self._num_lives} left.")
            return False
        
    def _update_word_guessed(self, guess):
        '''Updates the word_guessed list replacing the relevant underscores with the correctly guessed character.'''
        i = 0
        for character in self.word:
            if guess == self.word[i]:
                self.word_guessed[i] = character
            i += 1


def play_game(word_list: list) -> Hangman:
    num_lives = 5
    hangman = Hangman(word_list, num_lives)
    print(f"The word is: {hangman.display_word_guessed()}") #Display the initial amount of underscores

    while True:
        if hangman.get_num_lives() == 0:
            print(f"You lost! The word was \"{hangman.word}\"")
            break
        elif hangman.num_letters > 0:
            hangman.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

    
play_game(["Python", "Unity", "Unreal", "Programming", "Abstraction", "Testing"])