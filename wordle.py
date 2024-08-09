import json
import random
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)
class Wordle:
    def __init__(self):
        if sys.platform in ["linux", "linux2", "darwin"]:
            self.word_list = json.load(open("data/words.json"))
        elif sys.platform == "win32":
            self.word_list = json.load(open("data\\words.json"))
        else:
            print("Unknown platform")
            sys.exit()

        self.turns = 6  # Set the number of turns
        self.word = None

    def get_word(self):
        word = self.word_list[random.randint(0, len(self.word_list) - 1)]
        self.word = word
        return word

    def color(self, color: str, letter: str):
        if color == "green":
            print(Fore.GREEN + letter.upper(), end=" ")
        elif color == "yellow":
            print(Fore.YELLOW + letter.upper(), end=" ")
        else:
            print(Fore.LIGHTBLACK_EX + letter.upper(), end=" ")

    def check_word(self, guess: str):
        print("\n" + "-"*30)
        correct_word = list(self.word)
        guess_word = list(guess)
        result = [''] * 5

        # First pass: Check for correct (green) letters
        for i in range(5):
            if guess_word[i] == correct_word[i]:
                result[i] = 'green'
                correct_word[i] = None  # Mark this letter as used

        # Second pass: Check for present (yellow) letters
        for i in range(5):
            if result[i] == '':
                if guess_word[i] in correct_word:
                    result[i] = 'yellow'
                    correct_word[correct_word.index(guess_word[i])] = None  # Mark this letter as used
                else:
                    result[i] = 'grey'

        # Display the result
        for i in range(5):
            self.color(result[i], guess_word[i])

        print("\n" + "-"*30)

        return guess == self.word

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + Style.BRIGHT + "Welcome to Wordle!")
        print("Guess the 5-letter word within 6 attempts.\n")

        self.get_word()
        self.isGameOver = False

        for i in range(self.turns):
            if self.check_word(self.get_input()):
                break
        else:
            print(Fore.RED + Style.BRIGHT + f"\nGame Over! The correct word was: {self.word.upper()}\n")
