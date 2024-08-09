from wordle import Wordle
from player import Player
from computer import Computer
import random

def main():
    # Initialize the game
    game = Wordle()
    player = Player("Player 1")
    computer = Computer(word_list=game.word_list)
    
    # Set the word to be guessed by both player and computer
    game.set_word(random.choice(game.word_list))

    for turn in range(game.turns):
        print(f"\nTurn {turn + 1}/{game.turns}")

        # Player's turn
        player_guess = player.get_input()
        if game.check_word(player_guess):
            print(f"Congratulations, {player.name}! You guessed the word!")
            break

        # Computer's turn
        computer_guess = computer.get_input()
        if game.check_word(computer_guess):
            print(f"{computer.name} has guessed the word!")
            break
    else:
        print(f"Out of turns! The word was: {game.word.upper()}")

if __name__ == "__main__":
    main()
