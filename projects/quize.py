questions = [{
    "question": "What is the capital of France?",
    "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
    "answer": "C",
},
{    "question": "What is the largest planet in our solar system?",
    "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
    "answer": "B"
    },
{    "question": "What is the chemical symbol for water?",
    "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
    "answer": "A"}
]

score = 0
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer: ").strip().upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", q["answer"])
    print()

print("Your total score is:", score, "out of", len(questions))
print("Thank you for participating in the quiz!")    