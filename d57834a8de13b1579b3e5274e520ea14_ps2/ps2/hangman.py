# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # Open the file in read mode
    inFile =open(WORDLIST_FILENAME,"r")
    # Read the first line of the file
    line = inFile.readline()
    # Split the line into words and create a list of words
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    # Return the list of words
    return wordlist

# Load the list of words from the file
wordlist = load_words()


# Function to choose a random word from the wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# Initialize the list of words
wordlist = load_words()

# Function to check if the secret word is guessed
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for ch in secret_word:
        if ch  not in  letters_guessed:
            return False
        else:   
            return True
  


# Function to display the guessed word with underscores"_ "
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for ch in secret_word:
        if ch in letters_guessed:
            guessed_word += ch
        else:
            guessed_word += "_ "
    return guessed_word


# Function to get available letters that have not been guessed
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=""
    for ch in string.ascii_lowercase:
        if ch not in letters_guessed:
           available_letters += ch
    return available_letters
letters_guessed = [ ]
available_letters = get_available_letters(letters_guessed) 

    
    
# Hangman game function
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
     # Welcome message
    print("welcome to hangman game🙏")
    print("I am thinking of a word is letter long.",len(secret_word)) # initial hidden word
    print("_ _ _ _ _ _ _ _ _ _ _")
    # Initialize variables
    guesses_remaining = 6 # Number of guesses
    warning = 3  # Number of warnings
    letters_guessed=[] # List to store guessed letters
    # Main game loop
    while guesses_remaining > 0:
       # warnings and guesses remaining 
       print("Oops! You already guessed that letter😮. You have  warnings left💀. ",warning)
       print("you have a guess left.",guesses_remaining)
       print("Available letters: ",get_available_letters(letters_guessed))
       x = []
       letters = string.ascii_lowercase
       for i in  letters:
         if i in secret_word:
              x.append(i)
      # Check if the word has been completely guessed
       if (is_word_guessed(secret_word, letters_guessed)):
          print("Congratulations, you won🥳!")
          total = guesses_remaining *len(letters_guessed)
          print("Your total score for this game is: ",total)
          return ""
       else:
          guess=str(input("Please guess a letter🤔: "))  # user's guess
          if(guess.isalpha()):
             guess=guess.lower() # Convert guess to lowercase

             # Check if the letter has already guessed
             if (guess in letters_guessed ):
                 warning -=1
                 print("Oops! That is not a valid letter😖. You have warnings left💀.",warning)
                 if(warning<=0):
                     guesses_remaining-=1
             letters_guessed.append(guess) # Add the guess to the list of guessed letters

             # Check if the guessed letter is a vowel and not in the secret word
             if (guess in "aieou" and guess not in secret_word):
                guesses_remaining -=2
                print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))
                print("------------")
             else:
                # Check if the guessed letter is not in the secret word
                if (guess not in secret_word):
                    guesses_remaining-=1
                    print("Oops! That letter is not in my word😳: ",get_guessed_word(secret_word, letters_guessed))
                    print("----------")
                else:
                    print("Good guess🤩: ",get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
          else:
            if (guess==" ") :
              print(get_guessed_word(secret_word, letters_guessed))
            else:
              print("enter a valid guess")
              warning -=1
              if (warning<=0):
                  guesses_remaining-=1
     # If the player runs out of guesses
    if guesses_remaining == 0 :
       print("Sorry, you ran out of guesses😭. The word is:",secret_word)
       return ""


        
   


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


# Function to check if a partially guessed word matches possible words in the wordlist
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" "," ")
    if(len(my_word)==len(other_word)):
        for i in range(len(my_word)):
            if(my_word[i]=="_"):
              pass
            else:
               if(my_word[i]!=other_word[i]):
                   return False 
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    lists=[] 
    for ch in wordlist:
       if(match_with_gaps(my_word,ch)):
          lists.append(ch)
    return lists



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
