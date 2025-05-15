
import os

# Filename where we'll save the leaderboard scores
LEADERBOARD_FILE = 'leaderboard.txt'

# A list of quiz questions stored as dictionaries
questions = [
    {
        'question': "What is the capital of France?",
        'options': ['A) Paris', 'B) Rome', 'C) Madrid', 'D) Berlin'],
        'answer': 'A'
    },
    {
        'question': "Which language is used to write this program?",
        'options': ['A) Java', 'B) Python', 'C) C++', 'D) Ruby'],
        'answer': 'B'
    },
    {
        'question': "What does HTML stand for?",
        'options': ['A) Hyper Text Markup Language', 'B) High Text Machine Language', 'C) Hyper Tabular Markup Language', 'D) None of these'],
        'answer': 'A'
    },
    {
        'question': "Which of these is a Python data type?",
        'options': ['A) integer', 'B) tuple', 'C) float', 'D) All of the above'],
        'answer': 'D'
    },
    {
        'question': "What symbol is used to comment a single line in Python?",
        'options': ['A) //', 'B) #', 'C) <!-- -->', 'D) **'],
        'answer': 'B'
    }
]

def clear_screen():
    """
    Clears the terminal screen.
    Works on Windows and Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """
    Prints the main menu for the quiz game.
    """
    print("Welcome to the Python Quiz Game!")
    print("1. Start Quiz")
    print("2. View Leaderboard")
    print("3. Exit")

def get_user_choice():
    """
    Takes the user's menu choice and validates it.
    Only accepts 1, 2, or 3.
    """
    choice = input("Enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")
    return choice

def start_quiz():
    """
    Starts the quiz: asks user for their name,
    presents questions, validates answers,
    keeps score, and saves the result.
    """
    clear_screen()
    print("Starting Quiz...")
    name = input("Enter your name: ").strip()  # Strip removes extra spaces
    score = 0

    # Loop through all questions
    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for opt in q['options']:
            print(opt)

        # Get answer and validate input
        answer = input("Your answer (A/B/C/D): ").upper()
        while answer not in ['A', 'B', 'C', 'D']:
            answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

        # Check if the answer is correct
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz completed! {name}, your score is {score} out of {len(questions)}.")

    save_score(name, score)  # Save the score to leaderboard file
    input("\nPress Enter to return to the main menu...")

def save_score(name, score):
    """
    Save the player's name and score to the leaderboard file.
    If the file doesn't exist, it will be created.
    """
    try:
        with open(LEADERBOARD_FILE, 'a') as file:
            file.write(f"{name},{score}\n")
    except Exception as e:
        print("Error saving score:", e)

def view_leaderboard():
    """
    Reads and displays the top 5 scores from the leaderboard file.
    If no scores exist yet, informs the user.
    """
    clear_screen()
    print("Leaderboard (Top Scores):")
    if not os.path.exists(LEADERBOARD_FILE):
        print("No scores yet. Play the quiz first!")
    else:
        try:
            with open(LEADERBOARD_FILE, 'r') as file:
                scores = file.readlines()
            # Parse the scores and convert them to tuples (name, int_score)
            scores = [line.strip().split(',') for line in scores]
            scores = [(name, int(score)) for name, score in scores]
            # Sort by score descending
            scores.sort(key=lambda x: x[1], reverse=True)

            print("{:<20}{}".format("Name", "Score"))
            print("-" * 30)
            for name, score in scores[:5]:
                print(f"{name:<20}{score}")
        except Exception as e:
            print("Error reading leaderboard:", e)
    input("\nPress Enter to return to the main menu...")

def main():
    """
    Main program loop to display the menu and call other functions
    based on user input.
    """
    while True:
        clear_screen()
        print_menu()
        choice = get_user_choice()

        if choice == '1':
            start_quiz()
        elif choice == '2':
            view_leaderboard()
        else:
            print("Thanks for playing! Goodbye.")
            break

# Entry point of the program
if __name__ == "__main__":
    main()

