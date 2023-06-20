# imports
from operator import truediv
import random
from turtle import pos
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
word_length_offset = word_length - 1
end_of_game = False
lives = 6
display = []

# Print logo
print(logo)
print(f"There are {word_length} letters in the word.")

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(f"There are {word_length} letters in the word.")

    if guess in display:
        print(f"You've already guessed {guess}")
    
# Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life. You have {lives} guesses remaining.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])