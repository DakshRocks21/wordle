import json
import random

class Wordle():
    def __init__(self):
        self.word_list = json.load(open("python/words.json"))
    def getWord(self):
        word = self.word_list[random.randint(0, len(self.word_list) - 1)]
        return word



wordle = Wordle()
print(wordle.getWord())