# Rock Paper Scissors Lizard Spock Game

This is an enhanced version of the classic Rock Paper Scissors game, including additional choices (Lizard and Spock) for a more interesting experience. The game allows you to play against the computer with adjustable difficulty levels and displays the results in a detailed, easy-to-read table format.

## Features

- **Choices**: Rock, Paper, Scissors, Lizard, and Spock.
- **Difficulty Levels**: Choose from three difficulty settings:
  - **Easy**: Random choices by the computer.
  - **Medium**: The computer makes random choices.
  - **Hard**: Advanced computer behavior (could be enhanced with specific patterns).
- **Round Results**: Displays the outcome of each round, along with your and the computer's choices.
- **Final Score**: Displays the total score after all rounds.
- **Round-by-Round Table**: A table summarizing each round's results.
- **Custom Number of Rounds**: Play a custom number of rounds.

## How to Play

1. **Run the Game**: When you start the game, you'll be prompted to choose how many rounds you'd like to play.
2. **Select Difficulty**: You can choose between three difficulty levels: Easy, Medium, and Hard.
3. **Make Your Move**: You will be prompted to enter a number to represent your move:
   - 0: Rock
   - 1: Paper
   - 2: Scissors
   - 3: Lizard
   - 4: Spock
4. **Round Outcome**: After each round, the computer’s move and the round's result will be displayed.
5. **Game Over**: After all rounds are completed, the game will show the final score and a round-by-round table.

## Requirements

- Python 3.x
- `pyfiglet` for the ASCII art of the game title.
- `tabulate` for displaying round-by-round results in a table format.

To install the required dependencies, use the following:

```bash
pip install pyfiglet tabulate
