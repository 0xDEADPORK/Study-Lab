
quiz = (
    ("What is the capital of France?", "Paris", "London", "Berlin", 1),
    ("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", 2),
    ("Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", 2),
    ("What is 5 + 7?", "10", "12", "15", 2),
)

score = 0

print("Welcome to the 2D Tuple Quiz Game!")
print("Choose the correct option number for each question.\n")

for i, q in enumerate(quiz, 1):
    question, option1, option2, option3, correct = q
    print(f"Q{i}: {question}")
    print(f"1. {option1}")
    print(f"2. {option2}")
    print(f"3. {option3}")
    
    while True:
        try:
            answer = int(input("Your answer (1-3): "))
            if answer not in [1, 2, 3]:
                print("Please enter a valid option (1, 2, or 3).")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    if answer == correct:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was option {correct}.\n")

print(f"Quiz Over! Your total score is: {score}/{len(quiz)}")
