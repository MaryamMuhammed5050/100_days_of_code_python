
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print("\nTo win, guess the word before you lose all your lives.\n")

display = []
wrong_guesses = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(f"You've already guessed the letter '{guess}'. Pick another letter.")

    else:
        wrong_guesses.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("\nGenius, genius, genius! You won!")

        if guess not in chosen_word:
            lives -= 1

        if not end_of_game:
            if guess not in chosen_word:
                print(f"'{guess}' is not in the word. You lost 1 life.")

            print(f"Lives remaining: {lives}")

        if lives == 0:
            end_of_game = True
            print("You have lost all your lives. You lose!")
            print(f"\nThe word was '{chosen_word}'")

