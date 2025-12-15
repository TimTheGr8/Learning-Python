import art
import random

EasyLevelTurns = 10
HardLevelTurns = 5

def CompareGuess(userGuess, actualAnswer, turns):
    """Checks the user guess against the answer, returns the number of guesses remaining."""
    if userGuess > actualAnswer:
        print(f"Your guess is too high.")
        return turns - 1
    elif userGuess < actualAnswer:
        print(f"Your guess is too low.")
        return turns - 1
    else:
        print(f"You  guessed it! The number is {actualAnswer}")
        return turns

def SetDifficulty():
    difficultyNotChosen = True
    while difficultyNotChosen:
        level = input("Choose a difficulty. Type 'easy' for 10 guesses and 'hard' for 5 guesses: ").lower()
        if level != "easy" and level != "hard":
            print("That is not a valid entry. Please try again.")
            continue 
        elif level == "easy":
            return EasyLevelTurns
        elif level == "hard":
            return HardLevelTurns
        difficultyNotChosen = False
        
def StartGame():
    print(art.logo)
    numberOfGuesses = SetDifficulty()
    print("Welcome to the Number Guessing Game!\nI am thinking of a number from 1 - 100.")

    answer = random.randint(1, 100)
    print(f"CHEATER: {answer}")
    currGuess = 0
    while currGuess != answer:
        print(f"You have {numberOfGuesses} remiaing.")
        currGuess = int(input("What number do you think it is: "))
        numberOfGuesses = CompareGuess(currGuess, answer, numberOfGuesses)
        if numberOfGuesses <= 0:
            print(f"You were not able to guess the number. The number was {answer}")
            return
    

while input("Would you like to play Guess The Number, 'y' or 'n': ") == "y":
    print(" \n" * 20)
    StartGame()