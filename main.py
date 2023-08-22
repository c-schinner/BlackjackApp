import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    # Returns a random card from the deck
    cards = [
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    ]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Take a list of cards and returns the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, dealer_score):
    # This is going to compare the total cards in each hand and see who wins
    if player_score == dealer_score:
        return "Push"
    elif dealer_score == 0:
        return "Dealer has BlackJack, you LOSE"
    elif player_score == 0:
        return "Player has BlackJack, you WIN"
    elif player_score > 21:
        return "You have gone over 21, you LOSE"
    elif dealer_score > 21:
        return "Dealer has gone over 21, you WIN"
    elif player_score > dealer_score:
        return "You WIN"
    else:
        return "You LOSE"


def play_game():

    print(logo)
    player_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"  Your cards: {player_cards}, your score: {player_score}")
        print(f"  Dealer card : {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to hit, type 'n' to stand: ")
            if user_should_deal == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"  Your final hand: {player_cards}, your final score: {player_score}")
    print(f"  Dealers final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a hand of BlackJack? Type 'y', or 'n' : ") == 'y':
    os.system('cls')
    play_game()
