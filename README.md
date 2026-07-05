# Math Facts Test

A Python-based quiz program to test your knowledge of squares, cubes, and square roots with customizable difficulty levels and timing feedback.

## Features

- **Separate difficulty levels** for squares, cubes, and square roots
- **Mixed question types** - randomly tests all three categories
- **Timing tracking** - displays average time per question
- **Instant feedback** - shows if you're correct and reveals the answer if wrong
- **Score summary** - displays your final score and accuracy percentage

## Requirements

- Python 3.x

## Usage

```bash
python test.py
```

The program will prompt you for:
1. **Number of questions** - How many questions you want to answer
2. **Max value for squares** - Tests up to n² (e.g., enter 12 for questions like 12² = ?)
3. **Max value for cubes** - Tests up to n³ (e.g., enter 12 for questions like 12³ = ?)
4. **Max root value** - Tests square roots up to √n (e.g., enter 12 for √144 = ?)

Answer each question with an integer, and the program will track your time and score.

## Example Session

```
=== Math Facts Test ===

How many questions do you want? 5
Max value for squares (e.g., 12 for up to 12²): 10
Max value for cubes (e.g., 12 for up to 12³): 5
Max root value for square roots (e.g., 12 for √144): 10

Starting 5 questions...

Question 1: 7² = ? 49
✓ Correct!

Question 2: √144 = ? 12
✓ Correct!

...

=== Results ===
Score: 5/5 (100.0%)
Avg time per question: 2.34s
```
