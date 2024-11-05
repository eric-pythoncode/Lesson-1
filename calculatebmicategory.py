def calculatebmi(weight, height):
    try:
        bmi = weight / (height * 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."
    

def calculatebmicategory(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
    
def tracksteps(dailysteps):
    if dailysteps < 5000:
        return "You're not working enough, try to be more active."
    elif 5000 <= dailysteps < 10000:
        return "Good job! Try to hit atleast 10,000 steps for optimal health."
    else:
        return "Amazing! Keep up the good work!"
    

def trackcaloriesburned(caloriesburned):
    if caloriesburned < 200:
        return "Try to be a little bit more active to burn more calories"
    elif 200 <= caloriesburned < 500:
        return "Good effort! Keep working towards your fitness goals."
    else:
        return "Amazing! You're burning a lot of calories!"
    
    
def tracksleep(sleepduration):
    if sleepduration < 7:
        return "You're not getting enough sleep."
    elif sleepduration <= 7 < 9:
        return "Great! You're getting a healthy amount of sleep."
    else:
        return "You're getting lots of sleep, but be sure to balance it with activity."
    

def trackwaterintake(waterintake):
    if waterintake < 2000:
        return "You need to drink more water!"
    elif waterintake <= 2000 < 3000:
        return "Good job! It's good to stay hydrated."
    else:
        return "Great! You're drinking lots of water."

print("Welcome to Enhanced Health App")
print("This app helps track BMI, daily steps, water intake, calories burned, and sleep duration.")

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your weight (in meters): "))
dailysteps = int(input("Enter your daily step count: "))
waterintake = int(input("Enter your daily water intake (in ml): "))
caloriesburned = int(input("Enter your calories burned today: "))
sleepduration = float(input("Enter your sleep duration (in hours): "))


bmi = calculatebmi(weight, height)
bmicategory = calculatebmicategory(bmi)

print("Your BMI is: ", bmi, " (", bmicategory, ")." )


stepfeedback = tracksteps(dailysteps)
print(f"Daily steps: {dailysteps}")
print(stepfeedback)


waterfeedback = trackwaterintake(waterintake)
print(f"Water intake: {waterintake} ml.")
print(waterfeedback)


caloriesfeedback = trackcaloriesburned(caloriesburned)
print(f"Calories burned: {caloriesburned}")
print(caloriesburned)


sleepfeedback = tracksleep(sleepduration)
print(f"Time slept: {sleepduration} hours")
print(sleepfeedback)

print("\nStay healthy and active!")

