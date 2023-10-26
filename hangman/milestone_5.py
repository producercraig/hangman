# %%
import random

class Hangman:
    '''
    Initialises the Hangman class with the following attributes:
        - word_list (private): The list of words (str) to pick from for the game.
        - word (private): The word randomly selected from the word_list (via get_random_word()).
        - word_guessed (private): Initialised as a list with an underscore representing each unguessed character. Over the course of gameplay,
          the list is updated with correctly guessed characters replacing the relevant underscore.
        - num_letters: The number of unique letters in the selected word. Obtained via _get_unique_letter_count()
        - num_lives: The number of attempts the player has to correctly guess a character. Default = 5.
        - list_of_guesses: A list containing all valid guesses from the player over the duration of gameplay.
    '''
    def __init__(self, word_list: list, num_lives = 5):
        self._word_list = word_list
        self._word = self._get_random_word()
        self._word_guessed = ["_" for character in self._word] #List of underscores representing unguessed characters
        self.num_letters = self._get_unique_letter_count() #The number of UNIQUE letters in the word that have not been guessed yet
        self._num_lives = num_lives #Number of incorrect guesses allowed
        self._list_of_guesses = [] #A list of current guesses

    def ask_for_input(self):
        '''Public method which requests a single character input from the user and calls validate_guess and check_guess if the input is valid.'''
        guess = input("Please enter a single character:")
        if self._validate_guess(guess) == False: #Checks if guess is alphabetical and length == 1
            print("Invalid letter. Please enter a single alphabetical character.") 
        elif guess in self._list_of_guesses: #Checks if guess has already been guessed by testing presence in list_of_guesses
            print("You already tried that letter!")
        else: #Guess is valid and not present in existing guesses list
            self._list_of_guesses.append(guess)  
            if self._check_guess(guess):
                print(f"Correct guess! {self.display_word_guessed()}")   

    def get_num_lives(self) -> int:
        '''Public method for getting the number of lives. Prevents external modification.'''
        return self._num_lives
    
    def display_word_guessed(self) -> str:
        '''A method for displaying the word_guessed list in a readable format. Returns a string.'''
        word_guessed_string = "" 
        for character in self._word_guessed:
            word_guessed_string += (character + " ")
        word_guessed_string = word_guessed_string[0].upper() + word_guessed_string[1:] #Capitalise first letter
        return word_guessed_string
    
    def display_word(self) -> str:
        '''A public method for displaying the selected word with the first letter capitalised for presentation.'''
        word = self._word[0].upper() + self._word[1:] #Capitalise first letter
        return word
                
    def _get_random_word(self) -> str:
        '''Returns a random word from the word_list variable and formats it to lower case.'''
        word = random.choice(self._word_list)
        word = word.lower()
        #print(f"[*FOR TESTING PURPOSES*] The word is: {word}") #for testing
        return word
    
    def _get_unique_letter_count(self) -> int:
        '''Creates a set from each character in the selected word to determine the count of unique letters. Returns that number as an int.'''
        unique_set = set(self._word)
        return len(unique_set)

    def _validate_guess(self, guess) -> bool:
        '''Takes an inputted string and returns True if length is 1 and content is alphabetic.'''
        if len(guess) != 1:
            return False
        elif guess.isalpha() == False:
            return False
        else:
            return True
        
    def _check_guess(self, guess) -> bool:
        '''Takes the validated character and returns True/False depending on if the character is present in the random word.'''
        guess = guess.lower()

        if guess in self._word:
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
        for character in self._word:
            if guess == self._word[i]:
                self._word_guessed[i] = character
            i += 1


def play_game(word_list: list) -> Hangman:
    '''Method used to start gameplay. Accepts a word_list in the format of a list of strings.'''
    num_lives = 5
    hangman = Hangman(word_list, num_lives)
    print(f"The word is: {hangman.display_word_guessed()}") #Display the initial amount of underscores

    while True:
        if hangman.get_num_lives() == 0:
            print(f"You lost! The word was \"{hangman.display_word()}\"")
            break
        elif hangman.num_letters > 0:
            hangman.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

    
play_game(["Python", "Unity", "Unreal", "Programming", "Abstraction", "Testing"])