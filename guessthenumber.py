import random as r

print("GUESS THE NUMBER")

randomNumber = r.randint(1, 10)
print("The number is between 1 and 10")
print("You have five guesses")
attempts = 0
#print(randomNumber)
while attempts <= 4:
    UserNumber = int(input("What is your first number?"))
    attempts += 1

    if UserNumber == randomNumber:
        print("You guessed it right! You took", attempts, "attempts!")
        break
    elif UserNumber > randomNumber:
        print("Your number is too high")
    elif UserNumber < randomNumber:
        print("Your number is too low")
    if attempts > 4 and UserNumber != randomNumber:
        print("You lose! The number was ", randomNumber)