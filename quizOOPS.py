import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow',
                       'grapes':'purple',
                       'dragon fruit':'pink',
                       'mango':'yellow',
                       }
        
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            useranswer = input()

            if(useranswer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
            
            option = int(input("enter 0 if you want to play again, otherwise enter 1."))
            if(option):
                return "Hope you enjoyed the quiz!"
        
print("Welcome to fruit quiz!")
fq = FruitQuiz()
fq.quiz()