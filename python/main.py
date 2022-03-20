import json
import random
from sys import platform
import os
# The Game
class Wordle():
    def __init__(self):
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            self.word_list = json.load(open("python/words.json"))
        elif platform == "win32":
            self.word_list = json.load(open("python\words.json"))
        else:
            print("Unknown platform")
            exit()

        
    def getWord(self):
        word = self.word_list[random.randint(0, len(self.word_list) - 1)]
        self.word = word
        return word
    
    def getInput(self):
        user = input("Enter a word: ")
        return user

    def color(self, color:str, letter:str):
        if color == "green":
            print(f"\033[92m{letter}\033[00m", end=" ")
        elif color == "yellow":
            print(f"\033[93m{letter}\033[00m", end=" ")

    def checkWord(self, word: str):
        # Check is the input is 100% correct
        if word == self.word:
            for i in word:
                self.color("green", i)
            print("\nYou won!\n\n")
        else:
            return False

os.system("clear")
wordle = Wordle()
wordle.checkWord(wordle.getWord())