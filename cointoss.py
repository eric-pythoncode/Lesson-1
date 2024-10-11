import random

print("Coin toss")

print("Best of 3")

score = 0

count = 0

while count < 3:
    num = random.randint(1, 2) #1 head 2 tail
    guess = input("What is your guess? h/t (head/tails): ")
    
    if ((num == 1 and guess.lower() == "h") or (num == 2 and guess.lower() == "t")):
        print("You guessed it correctly! You scored a point")
        score += 1
        count += 1
    elif ((num == 2 and guess.lower() == "h") or (num == 1 and guess.lower() == "t")):
        print("You guessed it wrong... You don't score a point.")
        count+= 1
    else:
        print("Wrong input")
    

print("Your final score = ", score)
print("Thanks for playing")