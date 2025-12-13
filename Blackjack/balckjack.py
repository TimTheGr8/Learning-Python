import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def DealCard(hand):
    hand.append(random.choice(cards))

def CalculateScore(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        gameOver = True
        return 0
    elif 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def CompareScores(userScore, compScore):
    if compScore == userScore:
        message = f"It is a push!"
    elif compScore == 0:
        message = f"Dealer has blackjack. Dealer wins!"
    elif userScore == 0:
        message = f"You have blackjack. You win!"
    elif userScore > 21:
        message = f"You busted. You lose!"
    elif compScore > 21:
        message = f"The dealer busted. You win!"
    else:
        message = f"You have {userScore} and dealer has {compScore}."
        if userScore > compScore:
            message+= " You win!"
        else:
            message += " You lose!"
    print(message)

def StartGame():
    print(art.logo)
    playerHand = []
    dealerHand = []
    playerScore = -1
    dealerScore = -1
    isGameOver = False

    for _ in range(2):
        DealCard(playerHand)
        DealCard(dealerHand)

    while not isGameOver: 
        playerScore = CalculateScore(playerHand)
        dealerScore = CalculateScore(dealerHand)
        print(f"Your cards: {playerHand} current score: {playerScore}")
        print(f"Dealer first card: {dealerHand[0]}")
        
        if playerScore == 0 or dealerScore == 0 or playerScore > 21:
            isGameOver = True
        else:
            newCard = input("Do you want another card? 'y' or 'n'\n")
            if newCard == "y":
                DealCard(playerHand)
            else:
                isGameOver = True
    
    while dealerScore < 17 and dealerScore != 0:# and dealerScore < 17:
            DealCard(dealerHand)
            dealerScore = CalculateScore(dealerHand)

    print(f"Your final hand: {playerHand}, final score: {playerScore}")
    print(f"Computer's final hand: {dealerHand}, final score: {dealerScore}")
    print(CompareScores(playerScore, dealerScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    StartGame()