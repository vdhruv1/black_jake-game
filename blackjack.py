import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def current_sum(cards):
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def play_blackjack():
    user_cards = []
    computer_cards = []

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = current_sum(user_cards)
        computer_score = current_sum(computer_cards)

        print(f"Your cards: {user_cards}  Current value: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            if user_score == 0:
                print("Blackjack! You win!")
            elif computer_score == 0:
                print("Computer got Blackjack! You lose!")
            elif user_score > 21:
                print("You busted! You lose!")
            continue  # Skip to end of the loop

        user_deal = input("Do you want to draw another card? (y/n): ").strip().lower()
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    # Only run the computer's turn if the game isn't over
    if not is_game_over:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = current_sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score <= 21:
        if computer_score > 21 or user_score > computer_score:
            print("You win!")
        elif user_score == computer_score:
            print("It's a draw!")
        else:
            print("You lose!")
    else:
        print("You busted! You lose!")

while input("if you want to play more (yes/no)").strip().lower() =="yes":
    play_blackjack()






