import art
import random

numberToGuess = -1
difficulty = ""
numberOfGuesses = 0
numberGuessed = False
playing = True

def CompareGuess(guess):
    global playing
    global numberOfGuesses
    global numberToGuess
    message = ""
    if guess == numberToGuess:
        message = f"You  guessed it! The number is {numberToGuess}"
        playing = False
    elif guess > numberToGuess:
        message = f"Your guess is too high."
        numberOfGuesses -= 1
    elif guess < numberToGuess:
        message = f"Your guess is too low."
        numberOfGuesses -= 1
    print(message)
    
def StartGame():
    global numberToGuess
    global difficulty
    global numberOfGuesses
    global numberGuessed
    global playing
    playing = True
    numberToGuess = -1
    difficulty = ""
    numberOfGuesses = 0
    numberGuessed = False
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number from 1 - 100.")

    difficultyNotChosen = True
    while difficultyNotChosen:
        difficulty = input("Choose a difficulty. Type 'easy' for 10 guesses and 'hard' for 5 guesses: ").lower()
        if difficulty != "easy" and difficulty != "hard":
            print("That is not a valid entry. Please try again.")
            continue 
        elif difficulty == "easy":
                numberOfGuesses = 10
        elif difficulty == "hard":
            numberOfGuesses = 5
        difficultyNotChosen = False

    numberToGuess = random.randint(1, 100)
    print(f"CHEATER: {numberToGuess}")
    while playing:
        if numberOfGuesses > 0 and not numberGuessed:
            print(f"You have {numberOfGuesses} remiaing.")
            currGuess = input("What number do you think it is: ")
            CompareGuess(int(currGuess))
        else:
            playing = False
            print(f"You were not able to guess the number. The number was {numberToGuess}")

while input("Would you like to play Guess The Number, 'y' or 'n': ") == "y":
    print(" \n" * 20)
    StartGame()