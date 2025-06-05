import random

# Word list for the game
words = ["python", "developer", "hangman", "program", "challenge", "khushi", "variable"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character..")
        continue

    if guess in guessed_letters:
        print("yeahh! You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"oh no! Wrong guess. Attempts left: {attempts}")

    # Display the current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if the user has won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word!a:", word)
        break
else:
    print("\nGame Over. The word was:", word)