import random
import os
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw 🙃"
    elif user_score > 21 and computer_score > 21:
        return "You went over. You lose.😤"
    elif computer_score == 0:
        return("The opponent has a BlackJack. You Lose. 😱")
    elif user_score > 21:
        return("You went over 21 points. You Lose.😭")
    elif user_score == 0:
        return("You win!😎")
    elif computer_score > 21:
        return("The opponent went over 21 points. You win!😁.")
    elif user_score > computer_score:
        return("You win!😃")
    else:
        return("You Lose. 😤")

def play_game():

    print (logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

        
    while not is_game_over:        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, currenct score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score >21:
            is_game_over = True    
        else:
            draw_another_card = input("Do you want to draw another card? Type 'y' or 'n'")
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play BlackJack? Type 'y' or 'n'") == "y":
    os.system('cls')
    play_game()
