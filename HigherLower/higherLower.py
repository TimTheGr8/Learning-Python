import art
import data
import random

name1, name2, description1, description2 = "", "", "" ,""
names = []
descriptions = []
followers = []

""" 
select names from data file
ensure the names are not the same
assign the names and descriptions
"""
name1 = random.choice(list(data.people))
description1 = data.GetName()
def ChooesName():
    namePicked = False
    while not namePicked:
        temp = random.choice(list(data.people))
        if temp not in names:
            names.append(temp)
            namePicked = True



print(f"Name 1:{name1} description 1: {description1} \nName 2: {name2} description 2: {description2}")

question = f"Who has more followers:\nA) {name1} {description1}\nB) {name2} {description2}"
