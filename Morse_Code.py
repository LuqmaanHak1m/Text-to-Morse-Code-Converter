import winsound as ws
import time 

MORSE = [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".-- ","-..-","-.-- ","--.."]

# Frequency (in kHz)
FREQUENCY = 3

# Dot and dash lengths (in milliseconds)
DOT_LENGTH = 0.5
DASH_LENGTH = 1

# Time between parts of a letter and different letters (seconds)
TIME_BETWEEN_PARTS_OF_THE_SAME_LETTER = 0.5
TIME_BETWEEN_LETTERS = 1


def textToMorse(text: str):

    text = text.replace(" ", "")

    textList = list(text)

    # If the character is a number then just add it to the list
    # else find the unicode for the letter (leaving a 10 digit buffer for the numbers)
    textMorse = [int(char) if char.isdigit() else ord(char) - 87 for char in textList]

    # 8 = 8, 9 = 9, 10 = a, 11 = b ...
    morse = [MORSE[x] for x in textMorse]

    print(f"The morse for this is: {morse}")
    
    return morse

def morseToSound(text: str):

    morse = textToMorse(text)

    for letter in morse:

        for signal in letter:

            if signal == ".":
                ws.Beep(FREQUENCY * 1000, DOT_LENGTH * 1000)
            else:
                ws.Beep(FREQUENCY * 1000, DASH_LENGTH * 1000)

            time.sleep(TIME_BETWEEN_PARTS_OF_THE_SAME_LETTER)

        time.sleep(TIME_BETWEEN_LETTERS)
            

# User input

userInput = str(input("Enter text for conversion: "))

morseToSound(userInput)

