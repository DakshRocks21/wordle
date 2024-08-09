import json
import random
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

        self.turns = 6
        self.word = None

    def set_word(self, word: str):
        self.word = word.lower()

    def color(self, color: str, letter: str):
        if color == "green":
            print(Fore.GREEN + letter.upper(), end=" ")
        elif color == "yellow":
            print(Fore.YELLOW + letter.upper(), end=" ")
        else:
            print(Fore.LIGHTBLACK_EX + letter.upper(), end=" ")

    def check_word(self, guess: str):
        correct_guess = True
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                self.color("green", guess[i])
            elif guess[i] in self.word:
                self.color("yellow", guess[i])
                correct_guess = False
            else:
                self.color("grey", guess[i])
                correct_guess = False
        print()  # Newline after the word
        return correct_guess
