import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
fails = 0
word = random.choice(words).lower()
guessed = ("_ " * len(word)).split()
print("The category is animals")
print("This word has", len(word), "letters.")
print("".join(guessed))

while fails < 6:
    if "_" not in guessed:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()
    if guess in word and guess not in guessed:
        i = 0
        while i < len(word):
            if word[i] == guess:
                guessed[i] = guess
            i += 1
    else:
        if guess in word:
            print("You already guessed that letter.")
        else:
            print(guess, "is not in the word.")
            fails += 1
    print(hangman[fails])
    if fails == 6:
        print("You lose!")
        print("The word was", word)
    print("".join(guessed))
