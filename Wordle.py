# File: Wordle.py

"""
This file meets the requirements for milestone 2 by indicating if the word a user submits is 
valid or not. 
"""

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    gw = WordleGWindow()

    # Pick a random word as the answer
    answer = random.choice(FIVE_LETTER_WORDS)

    def enter_action(guess):
        # Convert the word to lowercase for consistency
        word = guess.lower()

        # Check if the entered word is exactly five letters long
        if len(word) != N_COLS:
            gw.show_message("Not enough letters")
            return

        

        # Check if the word is in the list of valid words
        if word in FIVE_LETTER_WORDS:
            gw.show_message("Valid word!")
            
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
import random

def wordle():
    gw = WordleGWindow()

    # Pick a random word as the answer
    answer = random.choice(FIVE_LETTER_WORDS)

    def enter_action(guess):
        guess = guess.lower()
        if len(guess) != N_COLS or guess not in FIVE_LETTER_WORDS:
            gw.show_message("Invalid word.")
            return

        # Initialize a list to keep track of colors for each letter
        colors = [MISSING_COLOR] * N_COLS

        # Check for correct letters in the correct place
        for i in range(N_COLS):
            if guess[i] == answer[i]:
                colors[i] = CORRECT_COLOR

        # Check for correct letters in the wrong place
        for i in range(N_COLS):
            if colors[i] == MISSING_COLOR and guess[i] in answer:
                # Only color it yellow if the letter is not already correctly used
                if answer.count(guess[i]) > guess[:i].count(guess[i]):
                    colors[i] = PRESENT_COLOR

        # Update the display with the appropriate colors
        for i in range(N_COLS):
            gw.set_square_color(0, i, colors[i])  # Assuming 0 is the current row

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
