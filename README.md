# Blackjack Game
Welcome to the Blackjack Game, a simplified version of the classic casino card game. Test your luck and strategy as you try to beat the dealer by getting closer to 21 without going over. Experience the thrill of hitting, standing, and comparing hands in this digital rendition of Blackjack.

# How to Play
Run the program using a Python interpreter (Python 3 recommended).
The game will display a logo and ask if you want to play a hand.
If you choose to play, you'll be dealt two cards as the player, and the dealer will receive one visible card.
You'll have the option to "hit" (draw another card) or "stand" (keep your current cards).
The goal is to get as close to 21 as possible without exceeding it.
The dealer will then play their hand according to the rules, hitting if their total is less than 17.
The program will determine the winner based on the final hands and display the result.

# Winning and Losing
If your score exceeds 21, you'll automatically lose.
If the dealer's score exceeds 21, you'll automatically win.
If both you and the dealer have the same score, it's a "push" (a tie).
If you have a score of 21 or the dealer has a score of 0 (Blackjack), you'll win.
If the dealer's score is closer to 21 than yours, you'll lose.

# Example Gameplay
Do you want to play a hand of Blackjack? Type 'y', or 'n' : y

Your cards: [11, 5], your score: 16
Dealer card : 10
Type 'y' to hit, type 'n' to stand: y

Your cards: [11, 5, 8], your score: 19
Dealer card : 10
Type 'y' to hit, type 'n' to stand: n

Your final hand: [11, 5, 8], your final score: 19
Dealers final hand: [10, 8], final score: 18
You WIN

# Note
If your hand has an Ace, it is considered an 11; if you would bust with the Ace as an 11 value, then the value automatically changes to a value of 1.

# Tips
Consider the total value of your cards and the dealer's visible card when deciding whether to hit or stand.
Keep track of the game state and your hand's score to make informed decisions.

# How to Run
Save the code to a .py file (e.g., blackjack_game.py).
Open a terminal or command prompt.
Navigate to the directory where the file is located.
Run the program by entering python blackjack_game.py.

Enjoy the excitement of Blackjack with the Blackjack Game and see if you can beat the dealer!






