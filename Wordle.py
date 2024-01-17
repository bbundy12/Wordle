# File: Wordle.py

"""
This file meets the requirements for milestone 3 by allowing the user to try to guess the word. It properly handles the 
coloring of the letters and displays the appropriate messages.
"""

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
import random

def wordle():

    gw = WordleGWindow()

    # Pick a random word as the answer
    sAnswer = "mushy"# random.choice(FIVE_LETTER_WORDS)
    print(sAnswer)

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
            iCurrentRow = gw.get_current_row()
          
            # Check for correct letters in the correct place
            for letter in range(N_COLS):
                sLetter = gw.get_square_letter(iCurrentRow, letter).lower()
                if sWord[letter] == sAnswer[letter]:
                    lColors[letter] = CORRECT_COLOR
                    # Update key color to green if not already set to green
                    if gw.get_key_color(sLetter.upper()) != CORRECT_COLOR:
                        gw.set_key_color(sLetter.upper(), CORRECT_COLOR)

                # Check for correct letters in the wrong place
                elif lColors[letter] == MISSING_COLOR and sWord[letter] in sAnswer:
                    # Only color it yellow if the letter is not already correctly used. This is done by comparing guesses
                    # up to but not including the current position.
                    if sAnswer.count(sWord[letter]) > sWord[:letter].count(sWord[letter]):
                        lColors[letter] = PRESENT_COLOR
                        # Update key color to yellow if it's not green or yellow
                        if gw.get_key_color(sLetter.upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
                            gw.set_key_color(sLetter.upper(), PRESENT_COLOR)
                else:
                # Set key to gray if it's not in the answer and not already colored
                    if gw.get_key_color(sLetter.upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
                        gw.set_key_color(sLetter.upper(), MISSING_COLOR)

            # Update the display with the appropriate colors
            for letter in range(N_COLS):
                gw.set_square_color(iCurrentRow, letter, lColors[letter])
            
            # Display congratulation message if the answer was guessed
            if sWord == sAnswer:
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
