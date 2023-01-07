import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    ## intentional bug in below line fixed by using .upper() on words. 
    # In our code we are checking with upper case so the words are required to be in uppercase as well.
    # Loved these intentional bugs, thanks Kylie Ying :)
    
    return word.upper() 

def hangman():
    word = get_valid_word(words)
    
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
       
        print("You have already used this letter: ", " ".join(used_letters))

        #what the user has already guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        # what current word is
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1
                print(f'oops wrong guess. {lives} left!')
        
        elif user_letter in used_letters:
            print("Your already guessed this letter. Choose something else.")
        
        else:
            print("Invalid character.")
        
    if(lives == 0):
        print(f'Oof you ran out of lives. Word was {word}! Better luck next time.')
    else:
        print(f"Correct! it was {word}")

hangman()
    

