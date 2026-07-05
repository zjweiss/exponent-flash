# Exponent Flash

A Python-based quiz program to test your knowledge of perfect squares, perfect cubes, and arbitrary exponents with customizable difficulty levels and timing feedback.

## Features

- **Perfect squares** - Find the square root of perfect squares (e.g., √144 = ?)
- **Perfect cubes** - Find the cube root of perfect cubes (e.g., ∛125 = ?)
- **Arbitrary exponents** - Calculate powers with customizable bases and exponents (e.g., 3^5 = ?)
- **Mixed question types** - Randomly tests all three categories
- **Timing tracking** - Displays average time per question
- **Instant feedback** - Shows if you're correct and reveals the answer if wrong
- **Score summary** - Displays your final score and accuracy percentage
- **Practice journal** - Saves each session with date, time, score, and wrong questions
- **Practice wrong answers** - Review questions you got wrong from specific sessions or all history
- **No duplicate questions** - Each question appears only once per session

## Requirements

- Python 3.x

## Usage

```bash
python test.py
```

### Main Menu

The program starts with a menu:

1. **Take a new quiz** - Start a fresh quiz with your chosen difficulty settings
2. **Practice wrong questions from a session** - Review questions you got wrong from a specific past session
3. **Practice all wrong questions from history** - Review all questions you've ever gotten wrong (no duplicates)

### New Quiz Settings

When taking a new quiz, you'll configure:
1. **Number of questions** - How many questions you want to answer
2. **Max base for perfect squares** - Highest base for perfect square questions (e.g., 12 tests up to 12²)
3. **Max base for perfect cubes** - Highest base for perfect cube questions (e.g., 5 tests up to 5³)
4. **Max exponent for base 2** - Maximum exponent for 2^n questions
5. **Max exponent for base 3** - Maximum exponent for 3^n questions
6. **Max exponent for base 4** - Maximum exponent for 4^n questions
7. **Max exponent for base 5** - Maximum exponent for 5^n questions

### Practice Journal

Each quiz session is automatically saved to `practice_log.json` with:
- Date and time of the session
- Your score and percentage
- All questions you answered incorrectly (for targeted practice)

## Example Sessions

### Taking a New Quiz

```
=== Exponent Flash ===

1. Take a new quiz
2. Practice wrong questions from a session
3. Practice all wrong questions from history

Choose an option (1-3): 1
How many questions do you want? 3
Max base for perfect squares (e.g., 12 for up to 12^2): 10
Max base for perfect cubes (e.g., 5 for up to 5^3): 5
Max exponent for base 2 (e.g., 7 for up to 2^7): 8
Max exponent for base 3 (e.g., 7 for up to 3^7): 6
Max exponent for base 4 (e.g., 7 for up to 4^7): 5
Max exponent for base 5 (e.g., 7 for up to 5^7): 4

Starting 3 questions...

Question 1: What is the square root of 144? 12
✓ Correct!

Question 2: 3^5 = ? 242
✗ Incorrect. The answer is 243

Question 3: What is the cube root of 27? 3
✓ Correct!

=== Results ===
Score: 2/3 (66.7%)
Avg time per question: 2.15s
```

### Practicing Wrong Questions

```
=== Exponent Flash ===

1. Take a new quiz
2. Practice wrong questions from a session
3. Practice all wrong questions from history

Choose an option (1-3): 3

Available sessions:

0: 2026-07-05 14:30:15 - Score: 2/3 (66.7%)

Practicing 1 wrong question(s)...

Question 1: 3^5 = ? 243
✓ Correct!

=== Results ===
Score: 1/1 (100.0%)
Avg time per question: 1.82s
```
