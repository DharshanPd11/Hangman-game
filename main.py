import random
import string
from words import words


def get_valid_word(words) :
    word= random.choice(words)              # chooses a random word from words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters =set(word)                #letters in the choosen word
    alphabet = set(string.ascii_uppercase) #inbuilt alphabets
    used_letters= set()                     #for storing used letters
    lives = 6

    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        print('you have',lives, 'lives left and you have used these letters : ',' '.join(used_letters))
        #showing current word
        word_list= [letter if letter in used_letters else '-' for letter in word  ]
        print("Current word : ",' '.join(word_list))
        user_letter =input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letters:
               word_letters.remove(user_letter)
           else:
               lives = lives  - 1
               print ("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already used this letter, Guess another one : ")

        else:
            print("Invalid character. Please try again.")
    if lives== 0:
        print("Sorry, The word was",word, "Game Over!, You died.")
    else:
        print("You have guessed the word",word," correctly !!")

hangman()

