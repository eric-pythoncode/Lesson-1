questions = [
    {
        "question": "What is the capital of Spain?"
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) vienna"]
        "answer": "c"
    },
    {
        "question": "How many people are on Earth?"
        "options": ["a) 8 billion", "b) 7 billion", "c) 6 billion", "d) 5 billion"]
        "answer": "a"
    },
    {
        "question": "What is the biggest sport?"
        "options": ["a) Baseball", "b) Volleyball", "c) Basketball", "d) Football"]
        "answer": "d"
    },
    {
        "question": "What is the capital of Spain?"
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) vienna"]
        "answer": "c"
    },
    {
        "question": "What is the speed of gravity?"
        "options": ["a) 9.8m/s", "b) 10m/s", "c) 9m/s", "d) 9.72m/s"]
        "answer": "a"
    },
    {
        "question": "How many states does USA have?"
        "options": ["a) 49", "b) 50", "c) 32", "d) 14"]
        "answer": "b"
    },
]

score = 0

print("Welcome to the quiz game")

for question in questions:
    print("\n" + question("question"))
    for option in question["options"]:
        print(option)

    answer = input("Pick either A, B, C or D.").lower

    if answer == question("answer"):
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was: ", question['answer'], "." )

print("Your final score is: ", score, " out of ", {len(questions)}, ".")