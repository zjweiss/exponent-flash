import random
import time
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = "practice_log.json"

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

def generate_question(q_type, max_square_base, max_cube_base,
                      exponent_limits, asked_questions):
    """Generate a random question that hasn't been asked yet."""
    while True:
        if q_type == 'perfect_square':
            num = random.randint(1, max_square_base)
            q_id = ('perfect_square', num)
        elif q_type == 'perfect_cube':
            num = random.randint(1, max_cube_base)
            q_id = ('perfect_cube', num)
        else:  # arbitrary exponent
            base = random.randint(2, 5)
            max_exp = exponent_limits[base]
            exponent = random.randint(2, max_exp)
            q_id = ('exponent', base, exponent)

        if q_id not in asked_questions:
            asked_questions.add(q_id)
            break

    if q_type == 'perfect_square':
        answer = num
        perfect_square = num ** 2
        question = f"What is the square root of {perfect_square}?"
    elif q_type == 'perfect_cube':
        answer = num
        perfect_cube = num ** 3
        question = f"What is the cube root of {perfect_cube}?"
    else:  # exponent
        base, exponent = q_id[1], q_id[2]
        answer = base ** exponent
        question = f"{base}^{exponent} = ?"

    return question, answer

def save_session(correct, num_questions, wrong_questions):
    """Save quiz session to log file."""
    session = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "score": f"{correct}/{num_questions}",
        "percentage": round((correct / num_questions * 100) if num_questions > 0 else 0, 1),
        "wrong_questions": wrong_questions
    }

    log = []
    if Path(LOG_FILE).exists():
        with open(LOG_FILE, 'r') as f:
            log = json.load(f)

    log.append(session)

    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

def load_log():
    """Load practice log from file."""
    if not Path(LOG_FILE).exists():
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)

def practice_wrong_questions(wrong_questions):
    """Practice only the questions that were answered incorrectly."""
    if not wrong_questions:
        print("No wrong questions to practice!\n")
        return

    print(f"Practicing {len(wrong_questions)} wrong question(s)...\n")

    correct = 0
    total_time = 0
    asked = set()

    for i, q_data in enumerate(wrong_questions):
        if q_data["q_id"] in asked:
            continue
        asked.add(q_data["q_id"])

        question = q_data["question"]
        answer = q_data["answer"]

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

    percentage = (correct / len(asked)) * 100 if len(asked) > 0 else 0
    avg_time = total_time / len(asked) if len(asked) > 0 else 0
    print(f"=== Results ===")
    print(f"Score: {correct}/{len(asked)} ({percentage:.1f}%)")
    print(f"Avg time per question: {avg_time:.2f}s\n")

def show_menu():
    """Show main menu and return user choice."""
    print("=== Exponent Flash ===\n")
    print("1. Take a new quiz")
    print("2. Practice wrong questions from a session")
    print("3. Practice all wrong questions from history\n")
    choice = input("Choose an option (1-3): ").strip()
    return choice

def show_sessions():
    """Show available sessions for practice."""
    log = load_log()
    if not log:
        print("No practice history found.\n")
        return None

    print("\nAvailable sessions:\n")
    for i, session in enumerate(log):
        print(f"{i}: {session['date']} {session['time']} - Score: {session['score']} ({session['percentage']}%)")

    choice = input(f"\nSelect session (0-{len(log)-1}): ").strip()
    try:
        idx = int(choice)
        if 0 <= idx < len(log):
            return log[idx]["wrong_questions"]
    except ValueError:
        pass

    print("Invalid choice.\n")
    return None

def quiz_session(max_square_base, max_cube_base, exponent_limits, num_questions):
    """Run a quiz session and return results."""
    print(f"\nStarting {num_questions} questions...\n")

    correct = 0
    question_types = ['perfect_square', 'perfect_cube', 'exponent']
    total_time = 0
    asked_questions = set()
    wrong_questions = []

    for i in range(num_questions):
        q_type = random.choice(question_types)
        question, answer = generate_question(q_type, max_square_base, max_cube_base,
                                             exponent_limits, asked_questions)

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
            wrong_questions.append({
                "question": question,
                "answer": answer,
                "user_answer": user_answer,
                "q_id": f"{q_type}_{question}"
            })

        total_time += elapsed_time

    percentage = (correct / num_questions) * 100 if num_questions > 0 else 0
    avg_time = total_time / num_questions if num_questions > 0 else 0
    print(f"=== Results ===")
    print(f"Score: {correct}/{num_questions} ({percentage:.1f}%)")
    print(f"Avg time per question: {avg_time:.2f}s\n")

    save_session(correct, num_questions, wrong_questions)

def main():
    choice = show_menu()

    if choice == "1":
        num_questions = get_positive_int("How many questions do you want? ")
        max_square_base = get_positive_int("Max base for perfect squares (e.g., 12 for up to 12^2): ")
        max_cube_base = get_positive_int("Max base for perfect cubes (e.g., 5 for up to 5^3): ")

        exponent_limits = {}
        for base in range(2, 6):
            exponent_limits[base] = get_positive_int(f"Max exponent for base {base} (e.g., 7 for up to {base}^7): ")

        quiz_session(max_square_base, max_cube_base, exponent_limits, num_questions)

    elif choice == "2":
        wrong_q = show_sessions()
        if wrong_q:
            practice_wrong_questions(wrong_q)

    elif choice == "3":
        log = load_log()
        all_wrong = []
        seen = set()
        for session in log:
            for q in session["wrong_questions"]:
                q_id = q.get("q_id")
                if q_id not in seen:
                    all_wrong.append(q)
                    seen.add(q_id)
        practice_wrong_questions(all_wrong)

    else:
        print("Invalid choice.\n")

if __name__ == "__main__":
    main()
