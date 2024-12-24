import random

class Hangman:
    HANGMAN_PICS = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\\  |
          / \\  |
              ===
        """
    ]

    def __init__(self, word_list):
        self.word_list = [word.upper() for word in word_list if word.isalpha()]  # Clean word list
        self.word = random.choice(self.word_list)  # Randomly choose a word
        self.mistakes = 0  # Number of wrong guesses
        self.new_word = ["_"] * len(self.word)  # Current guessed word
        self.guessed_letters = []  # Track letters already guessed

    def display_status(self):
        """Display the current game state."""
        print(self.HANGMAN_PICS[self.mistakes])  # Show current hangman state
        print(" ".join(self.new_word))  # Current progress
        print(f"Guessed letters: {', '.join(self.guessed_letters)}")

    def validate_guess(self, guess):
        """Validate the player's guess."""
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            return
        if guess in self.guessed_letters:
            print("You already guessed that letter.")
            return
        self.process_guess(guess)

    def process_guess(self, guess):
        """Process a valid guess."""
        self.guessed_letters.append(guess)
        if guess in self.word:
            print("That is a correct letter!")
            # Reveal the correct letters in new_word
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.new_word[index] = guess
        else:
            print("That letter is wrong.")
            self.mistakes += 1

    def is_game_over(self):
        """Check if the game has ended."""
        return self.mistakes == len(self.HANGMAN_PICS) - 1 or "_" not in self.new_word

    def play(self):
        """Start the game loop."""
        print("Welcome to Hangman!")
        self.display_status()

        while not self.is_game_over():
            guess = input("Enter a single letter: ").upper()
            self.validate_guess(guess)
            self.display_status()

        # End of game messages
        if "_" not in self.new_word:
            print("Congratulations! You guessed the word:", self.word)
        else:
            print(self.HANGMAN_PICS[-1])  # Show final hangman state
            print("Game Over! The word was:", self.word)

# Run the game
if __name__ == "__main__":
    word_list = ['Apples', 'Bananas', 'Strawberry', 'Kiwi', 'Grape', '123', 'Orange!', '', '']
    game = Hangman(word_list)
    game.play()
