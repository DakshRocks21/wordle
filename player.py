class Player:
    def __init__(self, name):
        self.name = name

    def get_input(self):
        user = input(f"{self.name}: Enter a 5-letter word: ").lower()
        while len(user) != 5 or not user.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            user = input(f"{self.name}: Enter a 5-letter word: ").lower()
        return user
