# File: Wordle.py

"""
This file meets the requirements for milestone 2 by indicating if the word a user submits is 
valid or not. 
"""

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    gw = WordleGWindow()

    def enter_action(sGuess):
         # Convert the word to lowercase for consistency
        sWord = sGuess.lower().strip()

        # Check if the entered word is exactly five letters long
        if len(sWord) != N_COLS:
            gw.show_message("Not enough letters")
        elif sWord in FIVE_LETTER_WORDS:
            gw.show_message("Valid word!")
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
