import random

class GuessingGame:
    """
    A class to represent the Number Guessing Game.
    
    Attributes:
    -----------
    times_to_play : int
        Number of times the game will be played (default is 5).
    max_play_limit : int
        Maximum limit for the number of times to play (default is 25).
    scores : list
        List to store the scores of the players and computer.
    """

    def __init__(self):
        """Initialize the game with default settings and an empty score list."""
        self.times_to_play = 5
        self.max_play_limit = 25
        self.scores = []

    def display_menu(self):
        """Display the main menu options to the user."""
        print("\nMenu:")
        print("1. Start Game")
        print("2. Setting")
        print("3. Score Statistics")
        print("4. Exit System")
        
    def start_game(self):
        """Start the game and handle user guesses."""
        
        nickname = input("Enter your nickname: ").strip()
        if nickname == "":
            print("Nickname cannot be empty. Please enter a valid nickname.")
            return self.start_game()
        
        
        secret_number = random.randint(1, 100)
        attempts = 0
        
        
        while attempts < 7:
            try:
                
                guess = int(input("Enter your guess (1-100): "))
                attempts += 1
                
                
                if guess < secret_number:
                    print("Guess higher")
                elif guess > secret_number:
                    print("Guess lower")
                else:
                    print("You got the number correctly!")
                    self.scores.append((nickname, attempts))
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 100.")
        
        
        if attempts >= 7:
            print("Computer wins!")
            self.scores.append(("Computer", attempts))
        
        
        self.times_to_play -= 1
        if self.times_to_play > 0:
            print(f"\nYou have {self.times_to_play} more times to play.")
            play_again = input("Press Enter to continue or type 'menu' to return to menu: ")
            if play_again.lower() != 'menu':
                return self.start_game()
            self.times_to_play = 5  
        else:
            self.times_to_play = 5  
        
        self.display_menu()
        self.menu_options()

    def settings(self):
        """Allow user to configure game settings."""
        print("\nSetting:")
        print("********")
        
        
        while True:
            try:
                new_times = int(input(f"Times to play (1-{self.max_play_limit}): "))
                if 1 <= new_times <= self.max_play_limit:
                    self.times_to_play = new_times
                    break
                else:
                    print(f"Please enter a value between 1 and {self.max_play_limit}.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        self.display_menu()
        self.menu_options()

    
    def get_score_value(self, score_tuple):
        """Return the second element (attempts) from a score tuple."""
        return score_tuple[1]

    def score_statistics(self):
        """Display high score board."""
        print("\nHigh Score Board")
        print("-------------------------------")
        
        
        
        sorted_scores = self.scores.copy()
        sorted_scores.sort(key=self.get_score_value)
        
        
        top_scores = sorted_scores[:3]
        
        
        for i in range(len(top_scores)):
            name = top_scores[i][0]
            score = top_scores[i][1]
            stars = '*' * score
            print(f"{i+1}. {name} ({score}) {stars}")
        
        self.display_menu()
        self.menu_options()

    def exit_system(self):
        """Exit the game system."""
        print("Exiting the system. Amazing game! We appreciate you playing")
        exit()

    def menu_options(self):
        """Handle menu selections."""
        while True:
            try:
                choice = int(input("Select an option (1-4): "))
                
                if choice == 1:
                    self.start_game()
                    break
                elif choice == 2:
                    self.settings()
                    break
                elif choice == 3:
                    self.score_statistics()
                    break
                elif choice == 4:
                    self.exit_system()
                else:
                    print("Invalid input! Please select a number between 1 and 4.")
            except ValueError:
                print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    game = GuessingGame()
    game.display_menu()
    game.menu_options()
