#7
import random

# Card deck and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Create deck
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate hand value
def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    for card in hand:
        if value > 21 and card[0] == 'Ace':
            value -= 10
    return value

# Game loop
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Player's hand: {player_hand} Total: {calculate_hand_value(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]} and a hidden card")

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        action = input("Hit or Stand (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print(f"Player's hand: {player_hand} Total: {calculate_hand_value(player_hand)}")
        elif action == 's':
            break

    if calculate_hand_value(player_hand) > 21:
        print("Player busts! Dealer wins!")
        return

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print(f"Dealer's hand: {dealer_hand} Total: {calculate_hand_value(dealer_hand)}")

    # Determine winner
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)
    if dealer_total > 21 or player_total > dealer_total:
        print("Player wins!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()



#5
import random

def score_roll(dice):
    score = 0
    counts = {i: dice.count(i) for i in range(1, 7)}
    for num in range(1, 7):
        if counts[num] >= 3:
            score += 1000 if num == 1 else num * 100
            counts[num] -= 3
    score += counts[1] * 100 + counts[5] * 50
    return score

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def play_game():
    score = 0
    target = 1000
    print("Welcome to Greed Dice Game!")

    while score < target:
        print(f"Current Score: {score}")
        input("Press Enter to roll the dice...")
        dice = roll_dice(6)
        print(f"Rolled dice: {dice}")
        roll_score = score_roll(dice)
        print(f"Points from this roll: {roll_score}")

        if roll_score == 0:
            print("No points! You bust!")
            continue
        score += roll_score
        
        decision = input("Roll again (r) or bank (b)? ").lower()
        if decision == 'b':
            print(f"You banked your points. Total score: {score}")
        if score >= target:
            print(f"\nCongratulations! You won with {score} points!")
            break

if __name__ == "__main__":
    play_game()
