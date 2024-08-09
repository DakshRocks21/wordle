import sys
import pygame
from wordle import Wordle
from player import Player
from computer import Computer

def terminal_game():
    game = Wordle()
    player = Player("Player 1")
    computer = Computer(word_list=game.word_list)

    secret_word = game.get_word()

    for turn in range(game.turns):
        print(f"\nTurn {turn + 1}/{game.turns}")

        player_guess = player.get_input()
        if game.check_word(player_guess):
            print(f"Congratulations, {player.name}! You guessed the word!")
            break

        computer_guess = computer.get_input()
        if game.check_word(computer_guess):
            print(f"{computer.name} has guessed the word!")
            break
    else:
        print(f"Out of turns! The word was: {secret_word.upper()}")

def gui_game():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Wordle GUI")

    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    grey = (192, 192, 192)
    
    game = Wordle()
    secret_word = game.get_word()
    guessed_words = []
    current_guess = ""
    turn = 0
    
    running = True
    while running:
        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(current_guess) == 5:
                        guessed_words.append(current_guess)
                        if game.check_word(current_guess):
                            running = False
                        current_guess = ""
                        turn += 1
                        if turn >= game.turns:
                            running = False
                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                elif event.unicode.isalpha() and len(current_guess) < 5:
                    current_guess += event.unicode.lower()
                    
        instructions = small_font.render("Type your guess and press Enter", True, white)
        screen.blit(instructions, (50, 50))
        
        y_offset = 150
        for guessed_word in guessed_words:
            for i in range(5):
                letter = guessed_word[i]
                if letter == secret_word[i]:
                    color = green
                elif letter in secret_word:
                    color = yellow
                else:
                    color = grey
                text = font.render(letter.upper(), True, color)
                screen.blit(text, (150 + i * 100, y_offset))
            y_offset += 100

        guess_text = font.render(current_guess.upper(), True, white)
        screen.blit(guess_text, (150, y_offset))

        pygame.display.flip()

    pygame.quit()
    print(f"Game Over! The word was: {secret_word.upper()}")


def main():
    print("Select Game Mode:")
    print("1. Terminal Game")
    print("2. GUI Game")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        terminal_game()
    elif choice == "2":
        gui_game()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
