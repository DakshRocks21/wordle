import random
from wordle import Wordle

class WordleAI:
    def __init__(self, word_list):
        self.word_list = word_list
        self.known_correct_positions = [""] * 5
        self.known_present_letters = []
        self.known_absent_letters = []
        self.possible_words = word_list

    def make_guess(self):
        if not self.known_correct_positions.count(""):
            return ''.join(self.known_correct_positions)
        
        filtered_words = []
        for word in self.possible_words:
            match = True
            for i, letter in enumerate(word):
                if self.known_correct_positions[i] and letter != self.known_correct_positions[i]:
                    match = False
                    break
                if letter in self.known_absent_letters:
                    match = False
                    break
                if letter in self.known_present_letters and letter not in word:
                    match = False
                    break
            if match:
                filtered_words.append(word)
        
        if filtered_words:
            guess = random.choice(filtered_words)
            self.possible_words = filtered_words
        else:
            guess = random.choice(self.possible_words)

        return guess

    def update_knowledge(self, word, feedback):
        for i, (letter, color) in enumerate(feedback):
            if color == "green":
                self.known_correct_positions[i] = letter
            elif color == "yellow":
                self.known_present_letters.append(letter)
            else:
                self.known_absent_letters.append(letter)

    def check_guess(self, guess, target_word):
        feedback = []
        for i in range(len(guess)):
            if guess[i] == target_word[i]:
                feedback.append((guess[i], "green"))
            elif guess[i] in target_word:
                feedback.append((guess[i], "yellow"))
            else:
                feedback.append((guess[i], "absent"))
        return feedback
