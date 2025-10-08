# Define the questions, options, and correct answers
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "prompt": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    print("Welcome to the Quiz Game!")

    for question in questions:
        print(f"\n{question['prompt']}")
        for option in question['options']:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.")
    
    print(f"\nQuiz finished! Your final score is {score} out of {len(questions)}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz(questions)