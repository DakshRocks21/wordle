import json
import random
from sys import platform


class Wordle():
    def __init__(self):
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            self.word_list = json.load(open("python/words.json"))
        elif platform == "win32":
            self.word_list = json.load(open("python\words.json"))
        else:
            print("Unknown platform")
        
    def getWord(self):
        word = self.word_list[random.randint(0, len(self.word_list) - 1)]
        return word



wordle = Wordle()
print(wordle.getWord())