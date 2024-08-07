import json, random, os
from sys import platform

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
        if word == self.word:
            for i in word:
                self.color("green", i)
            print("\nYou won!\n\n")
            self.isGameOver = True
        else:
            for i in range(len(word)):
                if word[i] == self.word[i]:
                    self.color("green", word[i])
                elif word[i] in self.word:
                    self.color("yellow", word[i])
                else:
                    print(word[i], end=" ")
            print("\n\n")


    def start(self):
        self.turns = 3
        self.isGameOver = False
        self.getWord()
        for i in range(self.turns):
            self.checkWord(self.getInput())
            if self.isGameOver == True:
                break

os.system("clear")
wordle = Wordle()
wordle.start()