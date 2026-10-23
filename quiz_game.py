
# Python Quiz Game

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. HTML", "D. CSS"],
        "answer": "B"
    },
    {
        "question": "What is 5 * 3?",
        "options": ["A. 8", "B. 10", "C. 15", "D. 20"],
        "answer": "C"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
        "answer": "B"
    }
]

score = 0

print("=== Python Quiz Game ===")

for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", item["answer"])

print(f"\nFinal Score: {score}/{len(questions)}")
