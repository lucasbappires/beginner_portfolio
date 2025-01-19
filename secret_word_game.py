import os
import platform

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def play_game():
    secret_word = 'python'
    guessed_letters = ''
    tries = 0

    print("Let's play a secret word game!")
    while True:
        typed_letter = input('Type a letter: ').lower()
        tries += 1

        if not typed_letter.isalpha():
            print("Don't type numbers or special characters!")
            continue
        if len(typed_letter) > 1:
            print('Only type one letter.')
            continue

        if typed_letter in secret_word:
            guessed_letters += typed_letter

        current_progress = ''
        for char_in_secret_word in secret_word:
            if char_in_secret_word in guessed_letters:
                current_progress += char_in_secret_word
            else:
                current_progress += '*'
        print(f'The secret word is "{current_progress}".')

        if current_progress == secret_word:
            clear_console()
            print('Good job, you found out the secret word!')
            print(f'The secret word is "{secret_word}".')
            print(f'It took you {tries} tries to find out the secret word.')
            break

if __name__ == '__main__':
    while True:
        play_game()        
        replay = input('Do you want to play again? (y/n) ').lower()
        if replay != 'y':
            break