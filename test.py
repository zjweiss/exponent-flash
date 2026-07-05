import random
import time

def get_positive_int(prompt):
    """Get a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_question(q_type, max_square, max_cube, max_root):
    """Generate a random question and return the question and answer."""
    if q_type == 'square':
        num = random.randint(1, max_square)
        answer = num ** 2
        question = f"{num}² = ?"
    elif q_type == 'cube':
        num = random.randint(1, max_cube)
        answer = num ** 3
        question = f"{num}³ = ?"
    else:  # square root
        num = random.randint(1, max_root)
        answer = num
        question = f"√{num ** 2} = ?"

    return question, answer

def main():
    print("=== Math Facts Test ===\n")

    num_questions = get_positive_int("How many questions do you want? ")
    max_square = get_positive_int("Max value for squares (e.g., 12 for up to 12²): ")
    max_cube = get_positive_int("Max value for cubes (e.g., 12 for up to 12³): ")
    max_root = get_positive_int("Max root value for square roots (e.g., 12 for √144): ")

    print(f"\nStarting {num_questions} questions...\n")

    correct = 0
    question_types = ['square', 'cube', 'sqrt']
    total_time = 0

    for i in range(num_questions):
        q_type = random.choice(question_types)
        question, answer = generate_question(q_type, max_square, max_cube, max_root)

        start_time = time.time()
        while True:
            try:
                user_answer = int(input(f"Question {i + 1}: {question} "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        elapsed_time = time.time() - start_time

        if user_answer == answer:
            print("✓ Correct!\n")
            correct += 1
        else:
            print(f"✗ Incorrect. The answer is {answer}\n")

        total_time += elapsed_time

    percentage = (correct / num_questions) * 100 if num_questions > 0 else 0
    avg_time = total_time / num_questions if num_questions > 0 else 0
    print(f"=== Results ===")
    print(f"Score: {correct}/{num_questions} ({percentage:.1f}%)")
    print(f"Avg time per question: {avg_time:.2f}s")

if __name__ == "__main__":
    main()
