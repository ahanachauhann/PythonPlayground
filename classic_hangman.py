#hangman game
import random

def hangman():
    words = ['python', 'hangman', 'game', 'word', 'guess']

    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6


    hidden_word = '_' * len(chosen_word)

    print('Welcome to Hangman!')
    print('The word contains', len(chosen_word), 'letters.')
    print(hidden_word)

    while True:
        guess = input('Enter a letter: ').lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print('You have already guessed that letter. Try again.')

            elif guess in chosen_word:

                hidden_word = ''.join([c if c == guess or c == hidden_word[i] else '_' for i, c in enumerate(chosen_word)])
                print(hidden_word)

                if '_' not in hidden_word:
                    print('Congratulations! You guessed the word correctly.')
                    break

            else:
                attempts -= 1
                print('Wrong guess. You have', attempts, 'attempts remaining.')

                if attempts == 0:
                    print('Game over! You ran out of attempts.')
                    print('The word was:', chosen_word)
                    break

            guessed_letters.append(guess)

        else:
            print('Invalid input. Please enter a single letter.')

hangman()
