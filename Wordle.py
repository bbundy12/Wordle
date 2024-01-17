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
    sAnswer = 'mushy' # random.choice(FIVE_LETTER_WORDS)
    print(sAnswer)  # For debugging purposes; remove or comment out in the final version

    def enter_action(sGuess):
        # Convert the word to lowercase and strip padding
        sWord = sGuess.lower().strip()

        # Check if the entered word is exactly five letters long
        if len(sWord) != N_COLS:
            gw.show_message("Not enough letters")
        elif sWord not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            # Creating a list of colors, setting each square to the default of gray
            lColors = [MISSING_COLOR] * N_COLS
            iCurrentRow = gw.get_current_row()

            # Count the occurrences of each letter in the answer
            answer_letter_count = {}
            for letter in sAnswer:
                answer_letter_count[letter] = answer_letter_count.get(letter, 0) + 1

            # Check for correct letters in the correct place and update counts
            for letter in range(N_COLS):
                sLetter = gw.get_square_letter(iCurrentRow, letter).lower()
                if sWord[letter] == sAnswer[letter]:
                    lColors[letter] = CORRECT_COLOR
                    answer_letter_count[sLetter] -= 1
                    if gw.get_key_color(sLetter.upper()) != CORRECT_COLOR:
                        gw.set_key_color(sLetter.upper(), CORRECT_COLOR)

            # Check for correct letters in the wrong place
            for letter in range(N_COLS):
                sLetter = gw.get_square_letter(iCurrentRow, letter).lower()
                if lColors[letter] == MISSING_COLOR and sWord[letter] in sAnswer:
                    if answer_letter_count[sWord[letter]] > 0:
                        lColors[letter] = PRESENT_COLOR
                        answer_letter_count[sWord[letter]] -= 1
                        if gw.get_key_color(sLetter.upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
                            gw.set_key_color(sLetter.upper(), PRESENT_COLOR)
                    elif gw.get_key_color(sLetter.upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
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
