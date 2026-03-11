# number-guessing-game-python

Number Guessing Game (Python)

Introduction
The Number Guessing Game is a Python application where the user predicts a randomly chosen number between 1 and 100. The game provides feedback for each guess and tracks total attempts. The user wins if they guess correctly within seven tries; otherwise, the machine wins.

Aim
To develop an engaging, user-friendly game that lets players guess a computer-generated number, modify settings, and view top scores. The project teaches important programming concepts like loops, conditionals, input validation, and random number generation.

Requirements
- Python 3.x
- Menu-driven console interface
- Input validation and error handling
- High-score tracking (top 3 scores)
- Adjustable number of game rounds

Problem Analysis
- Generate a random number between 1–100.
- Track number of attempts and provide feedback (“too high” / “too low”).
- Menu for starting the game, changing settings, viewing high scores, and exiting.
- Score tracking for both player and computer.

Solving Strategy
- Create a `GuessingGame` class containing game logic and data.
- Methods to display the menu, start the game, adjust settings, view high scores, and exit.
- Loop to handle user input and menu navigation.
- Generate random numbers and provide feedback based on guesses.
- Determine winner and update high-score list.
- Validate user input and handle errors gracefully.

Design & Methodology

Class: `GuessingGame`  

Attributes:  
- `times_to_play` – number of rounds (default 5)  
- `max_play_limit` – maximum allowed rounds (default 25)  
- `scores` – list storing player and computer results  

Methods:  
- `__init__()` – initializes game  
- `display_menu()` – shows main menu  
- `start_game()` – handles guessing gameplay  
- `settings()` – lets user set number of rounds  
- `score_statistics()` – displays top 3 scores  
- `exit_system()` – exits the game  
- `menu_options()` – handles menu choice execution  

Testing & Results
- Methods were tested individually and integrated via menu navigation.
- User evaluation ensured ease of input and navigation.
- Correct input handling, high-score tracking, and error messages confirmed.
- Game allows completion within seven attempts; scores saved and displayed accurately.
- Settings properly adjusted and applied.

Problems & Solutions
- Problem: Non-numeric or out-of-range inputs  
  Solution: Added robust input validation  
- Problem: Blank nickname  
  Solution: Added nickname validation prompting user for a proper name

Achievements
- Fully functional game with user-friendly interface.
- Reliable error handling and accurate score tracking.
- Simple to maintain with well-organized code and documentation.

Future Improvements
- Add advanced options (number ranges, difficulty levels)
- Multiplayer mode for multiple players
- Graphical User Interface (GUI) for enhanced user experience
