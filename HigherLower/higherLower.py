import art
import data
import random

def ChooesName(_names, _descriptions, _followers):
    """Adds a name to the names array as long as it is not already in the array"""
    namePicked = False
    while not namePicked:
        temp = random.choice(list(data.people))
        if temp not in _names:
            _names.append(temp)
            _descriptions.append(data.GetDescription(temp))
            _followers.append(data.GetFollowers(temp))
            namePicked = True

def GetAnswer(_followers):
    """Returns the correct answer for who has the most followers"""
    if _followers[0] > _followers[1]:
        return "a"
    else:
        return "b"

def NextName(_names, _descriptions, _followers):
    """Removes the first name and gets a new second name"""
    _names.pop(0)
    _descriptions.pop(0)
    _followers.pop(0)
    ChooesName(_names, _descriptions, _followers)


def StartGame():
    names = []
    descriptions = []
    followers = []
    answer = ""
    score = 0
    gameRunning = True

    for i in range(2):
        ChooesName(names, descriptions, followers)
    answer = GetAnswer(followers)
    
    while gameRunning:
        print(art.logo)
        print(f"Your current score: {score}")
        userAnswer = input(f"'A' or 'B'\nA) {names[0]} a {descriptions[0]} or\nB) {names[1]} a {descriptions[1]}\nWho has more followers: ").lower()
        if userAnswer == answer:
            print("You are correct!")
            NextName(names, descriptions, followers)
            answer = GetAnswer(followers)
            score += 1
            print("\n" * 20)
        else:
            print("\n" * 20)
            gameRunning = False
            print(f"Your final score is {score}")
        

StartGame()