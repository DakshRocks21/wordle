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
        
    def get_word(self):
        word = self.word_list[random.randint(0, len(self.word_list) - 1)]
        self.word = word
        return word

    def get_input(self):
        user = input(Fore.CYAN + "Enter a 5-letter word: ").lower()
        while len(user) != 5 or not user.isalpha():
            print(Fore.RED + "Invalid input. Please enter a 5-letter word.")
            user = input(Fore.CYAN + "Enter a 5-letter word: ").lower()
        return user

    def color(self, color: str, letter: str):
        if color == "green":
            print(Fore.GREEN + letter.upper(), end=" ")
        elif color == "yellow":
            print(Fore.YELLOW + letter.upper(), end=" ")
        else:
            print(Fore.LIGHTBLACK_EX + letter.upper(), end=" ")

    def check_word(self, word: str):
        print("\n" + "-"*30)
        if word == self.word:
            for i in word:
                self.color("green", i)
            print("\n" + Fore.GREEN + Style.BRIGHT + "\nCongratulations! You guessed the word!\n")
            return True
        else:
            for i in range(len(word)):
                if word[i] == self.word[i]:
                    self.color("green", word[i])
                elif word[i] in self.word:
                    self.color("yellow", word[i])
                else:
                    self.color("grey", word[i])
            print("\n" + "-"*30 + "\n")
            return False

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + Style.BRIGHT + "Welcome to Wordle!")
        print("Guess the 5-letter word within 6 attempts.\n")
        
        self.get_word()
        self.turns = 6
        self.isGameOver = False

        for i in range(self.turns):
            if self.check_word(self.get_input()):
                break
        else:
            print(Fore.RED + Style.BRIGHT + f"\nGame Over! The correct word was: {self.word.upper()}\n")
