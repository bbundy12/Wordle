# File: Wordle.py

"""
This file meets the requirements for milestone 2 by indicating if the word a user submits is 
valid or not. 
"""

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
import random

def wordle():

    gw = WordleGWindow()

    # Pick a random word as the answer
    sAnswer = random.choice(FIVE_LETTER_WORDS)

    def enter_action(sGuess):
        # Convert the word to lowercase. Strip is used to get rid of the padding
        sWord = sGuess.lower().strip()

       # Check if the entered word is exactly five letters long
        if len(sWord) != N_COLS:
            gw.show_message("Not enough letters")
        elif sWord not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
         # Creating a list of colors and setting each square to the default of grey
            lColors = [MISSING_COLOR] * N_COLS

            # Check for correct letters in the correct place
            for letter in range(N_COLS):
                if sGuess[letter] == sAnswer[letter]:
                    lColors[letter] = CORRECT_COLOR

            # Check for correct letters in the wrong place
            for letter in range(N_COLS):
                if lColors[letter] == MISSING_COLOR and sGuess[letter] in sAnswer:
                    # Only color it yellow if the letter is not already correctly used. This is done by comparing guesses
                    # up to but not including the current position.
                    if sAnswer.count(sGuess[letter]) > sGuess[:letter].count(sGuess[letter]):
                        lColors[letter] = PRESENT_COLOR

            # Update the display with the appropriate colors
            iCurrentRow = gw.get_current_row()
            for letter in range(N_COLS):
                gw.set_square_color(iCurrentRow, letter, lColors[letter])
            
            # Display congratulation message if the answer was guessed
            if sGuess == sAnswer:
                gw.show_message("Nice job!!")
            elif iCurrentRow < N_ROWS:
                iCurrentRow += 1
                gw.set_current_row(iCurrentRow)
            else:
                gw.show_message("Better luck next time")
                

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
