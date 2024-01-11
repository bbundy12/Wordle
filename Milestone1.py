# File: Wordle.py

"""
This file fulfills milestone 1. It fills the first row of the guessing board with a random word from the given
word list. 
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()

    # Pick a random word from the list of five-letter words
    chosen_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Display the chosen word in the first row of boxes
    for i in range(N_COLS):
        letter = chosen_word[i]
        gw.set_square_letter(0, i, letter)

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
