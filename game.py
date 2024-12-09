import random
#import pyfiglet
from tabulate import tabulate

# Display the title of the game
#app = pyfiglet.figlet_format("Rock Paper Scissors Lizard Spock")
#print(app)

# Choices for the game (with added Lizard and Spock)
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
outcome_dict = {
    ("Rock", "Scissors"): "Rock crushes Scissors",
    ("Rock", "Lizard"): "Rock crushes Lizard",
    ("Paper", "Rock"): "Paper covers Rock",
    ("Paper", "Spock"): "Paper disproves Spock",
    ("Scissors", "Paper"): "Scissors cuts Paper",
    ("Scissors", "Lizard"): "Scissors decapitates Lizard",
    ("Lizard", "Spock"): "Lizard poisons Spock",
    ("Lizard", "Paper"): "Lizard eats Paper",
    ("Spock", "Scissors"): "Spock smashes Scissors",
    ("Spock", "Rock"): "Spock vaporizes Rock"
}

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice, computer_choice) in outcome_dict:
        return f"You won! {outcome_dict[(player_choice, computer_choice)]}"
    else:
        return f"Computer won! {outcome_dict[(computer_choice, player_choice)]}"

# Function to handle computer's behavior (easy, medium, hard)
def get_computer_choice(difficulty):
    if difficulty == "easy":
        return random.choice(choices)
    elif difficulty == "medium":
        return random.choice(choices)
    elif difficulty == "hard":
        return random.choice(choices)

# Function to play the game
def game():
    score_player = 0
    score_computer = 0
    total_rounds = 0
    rounds_data = []

    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    rounds = int(input("How many rounds would you like to play? (e.g. 3 for best-of-three): "))
    
    print("Select difficulty (easy/medium/hard):")
    difficulty = input("Enter your choice: ").lower()

    for round in range(1, rounds + 1):
        print(f"\nRound {round}/{rounds}")

        # Input validation for user choice
        while True:
            try:
                print("\nChoose your move:")
                print("0: Rock")
                print("1: Paper")
                print("2: Scissors")
                print("3: Lizard")
                print("4: Spock")
                player_input = int(input("Enter the number for your choice: "))

                if player_input < 0 or player_input > 4:
                    raise ValueError("Invalid input. Please enter a number between 0 and 4.")
                
                player_choice = choices[player_input]
                break
            except ValueError as e:
                print(e)

        # Get computer's choice based on difficulty
        computer_choice = get_computer_choice(difficulty)

        print(f"\nYou chose: {player_choice}")
        print(f"The computer chose: {computer_choice}")
        
        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Update scores
        if "You won" in result:
            score_player += 1
        elif "Computer won" in result:
            score_computer += 1
        
        # Collect round data
        rounds_data.append([round, player_choice, computer_choice, result])
        total_rounds += 1
    
    # Display results in a table format
    print("\nFinal Score:")
    print(f"You: {score_player} | Computer: {score_computer}")
    
    # Display round-by-round results in a table
    headers = ["Round", "Your Choice", "Computer's Choice", "Result"]
    print("\nRound-by-Round Results:")
    print(tabulate(rounds_data, headers=headers, tablefmt="fancy_grid"))

    if score_player > score_computer:
        print("\nCongratulations, you won the game!")
    elif score_player < score_computer:
        print("\nSorry, the computer won the game.")
    else:
        print("\nIt's a tie!")

# Main function to control game flow
def main_menu():
    while True:
        print("\nSelect Game Mode:")
        print("1: Player vs Computer")
        print("2: Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            game()
        elif choice == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

# Start the main menu
main_menu()
