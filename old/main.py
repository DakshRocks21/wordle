import os
from wordle import Wordle
from old.wordle_ai import WordleAI
from colorama import Fore, Style, init

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Wordle!\n")
    print("1. Play against the computer")
    print("2. Exit")

    choice = input("\nChoose an option (1/2): ").strip()
    return choice

def play_vs_computer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Wordle: Player vs Computer\n")

    # Initialize the game and AI
    player_game = Wordle()
    word_list = player_game.word_list
    ai = WordleAI(word_list)

    # Set secret words
    player_word = input(Fore.CYAN + "Player: Enter your secret 5-letter word: ").lower()
    while len(player_word) != 5 or not player_word.isalpha():
        print(Fore.RED + "Invalid input. Please enter a 5-letter word.")
        player_word = input(Fore.CYAN + "Player: Enter your secret 5-letter word: ").lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')

    ai_word = player_game.get_word()
    print(Fore.YELLOW + f"The computer has chosen its secret word.\n")

    player_game.set_word(ai_word)
    ai_target_word = player_word

    player_attempts_left = player_game.turns
    ai_attempts_left = player_game.turns
    player_won = False
    ai_won = False

    while player_attempts_left > 0 and ai_attempts_left > 0 and not (player_won or ai_won):
        print(f"Attempts left: Player: {player_attempts_left} | Computer: {ai_attempts_left}\n")
        
        # Player's turn to guess the computer's word
        print("Player's guess:")
        player_guess = player_game.get_input(1)
        player_won = player_game.check_word(player_guess)

        # Computer's turn to guess the player's word
        print("Computer's guess:")
        ai_guess = ai.make_guess()
        print(Fore.MAGENTA + ai_guess.upper())

        # AI updates its knowledge based on the feedback
        ai_feedback = ai.check_guess(ai_guess, ai_target_word)
        ai.update_knowledge(ai_guess, ai_feedback)

        ai_won = (ai_guess == ai_target_word)

        if player_won:
            print(Fore.GREEN + "Player wins!")
        elif ai_won:
            print(Fore.RED + "Computer wins!")
        
        player_attempts_left -= 1
        ai_attempts_left -= 1

    if not player_won and not ai_won:
        print(Fore.RED + "Both ran out of attempts. It's a draw!")
        print(Fore.GREEN + f"Computer's word was: {ai_word.upper()}")
        print(Fore.RED + f"Player's word was: {player_word.upper()}")

def main():
    while True:
        choice = menu()
        if choice == "1":
            play_vs_computer()
        elif choice == "2":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
