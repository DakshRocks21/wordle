from wordle import Wordle
from player import Player
from computer import Computer

def main():
    # Initialize the game
    game = Wordle()
    player = Player("Player 1")
    computer = Computer(word_list=game.word_list)
    
    # Get the word to be guessed
    secret_word = game.get_word()

    for turn in range(game.turns):  # The game.turns is now properly initialized
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
        print(f"Out of turns! The word was: {secret_word.upper()}")

if __name__ == "__main__":
    main()
