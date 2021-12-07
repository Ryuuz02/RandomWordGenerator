# Import Statements
from random import randint
import enchant


# Function to randomly choose a word, weighted based on frequency of word lenghts
def choose_word():
    random_num = randint(1, 232400)
    if random_num < 50:
        return 1
    elif random_num < 150:
        return 2
    elif random_num < 1150:
        return 3
    elif random_num < 6450:
        return 4
    elif random_num < 16450:
        return 5
    elif random_num < 16450:
        return 6
    elif random_num < 33950:
        return 7
    elif random_num < 57450:
        return 8
    elif random_num < 87450:
        return 9
    elif random_num < 119450:
        return 10
    elif random_num < 150150:
        return 11
    elif random_num < 175650:
        return 12
    elif random_num < 195650:
        return 13
    elif random_num < 210650:
        return 14
    elif random_num < 220650:
        return 15
    elif random_num < 226650:
        return 16
    elif random_num < 229950:
        return 17
    elif random_num < 231450:
        return 18
    elif random_num < 231950:
        return 19
    elif random_num < 232200:
        return 20
    else:
        return 21


# Checks if a word is valid
def check_word_validity(input_word):
    return d.check(input_word)


# Dictionary for checking word validity
d = enchant.Dict("en_US")
# List of all english alphabet to make words
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
# Controller for main loop to find when it hits a valid word
bad_word = True
# Main Loop
while bad_word:
    # Randomly generates word_length
    word_length = choose_word()
    # Sets the word equal to blank string
    word = ""
    for i in range(0, word_length):
        # For each letter in the word, adds a random letter
        word += alphabet_list[randint(0, 25)]
    # Checks to see if the word is valid
    if check_word_validity(word):
        # If it is, ends the loop
        bad_word = False
# Prints the valid word
print(word)
