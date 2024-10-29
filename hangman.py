import random
words = ["tacos", "rice", "chocolate", "steak"]

secretword = random.choice(words)
guessedletters = []
attempts = 6

print("Welcome to Hangman!")
print("The letter is related to food")

print("_ " * len(secretword))

while attempts > 0:
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter")
        continue
    if guess in guessedletters:
        print("You have already guessed that number. Try again.")
        continue
    guessedletters.append(guess)

    if guess in secretword:
        print("Good guess. ", guess)
    else:
        attempts -= 1
        print("Wrong guess. You have ", attempts, " attempts now.")

    currentstate = "".join(letter if letter in guessedletters else "_" for letter in secretword)
    print("Current word: ", " ".join(currentstate))

    if "_" not in currentstate:
        print("Congratulations! You have guessed the word ", secretword, "!")
else:
    print("You lost! The word was: ", secretword, ".")