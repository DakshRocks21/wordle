import random
from player import Player

class Computer(Player):
    def __init__(self, name="Computer", word_list=None):
        super().__init__(name)
        self.word_list = word_list

    def get_input(self):
        word = random.choice(self.word_list)
        print(f"{self.name}: Computer guessed the word {word.upper()}")
        return word.lower()
