import random

# Hangman - Games
words = ["Overwatch", "Valorant", "ROV"]
lives = 5
word = random.choice(words).lower()
guessed = ["_"] * len(word)
print("This word has", len(word), "letters.")
print("".join(guessed))

while lives > 0:
    if "_" not in guessed:
        break

    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print(guess, "is not in the word.")
        lives -= 1
    if lives == 4:
        print("  O")
    elif lives == 3:
        print("  O")
        print("  |")
    elif lives == 2:
        print("  O")
        print(" \|")
    elif lives == 1:
        print("  O")
        print(" \|/")
    elif lives == 0:
        print("  O")
        print(" \|/")
        print(" /\\")
        print("You lose!")
        print("The word was", word)
    print("".join(guessed))
