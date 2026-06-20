import random

def play_hangman():
    words_pool = ["python", "coding", "intern", "stocks", "chatbot"]
    secret_word = random.choice(words_pool).lower()
    guessed_letters = []
    incorrect_guesses_left = 6

    print("Welcome to the Hangman Game!")
    print("Try to guess the secret word letter by letter.")

    while incorrect_guesses_left > 0:
        print("\n-----------------------------")
        
        displayed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        
        print("Word to guess:", displayed_word.strip())
        print("Remaining guesses:", incorrect_guesses_left)
        print("Guessed letters:", ", ".join(guessed_letters))

        if "_" not in displayed_word:
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good job! That letter is in the word.")
        else:
            print("Wrong guess!")
            incorrect_guesses_left -= 1

    else:
        print("\n-----------------------------")
        print("Game Over! You ran out of guesses.")
        print("The correct word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
