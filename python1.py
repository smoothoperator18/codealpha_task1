import random

words = ["python", "hangman", "random", "simple", "game"]
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
max_attempts = 6
wrong_attempts = 0

print("Welcome to Hangman!")
print("You need to guess the word.")
print("The Word to guess: ", " ".join(guessed_word))

while wrong_attempts < max_attempts and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess! Attempts left:", max_attempts - wrong_attempts)
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)