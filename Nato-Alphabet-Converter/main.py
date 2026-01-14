import pandas

alpha_data = pandas.read_csv("Nato-Alphabet-Converter/nato_phonetic_alphabet.csv")
natobet = {row.letter: row.code for (index, row) in alpha_data.iterrows()}

# word = input("Enter a word: ").upper()

incorrect_input = True
while incorrect_input:
    word = input("Enter a word: ").upper()
    try:
        response = [natobet[letter] for letter in word]
    except KeyError:
        print("Please only enter letters in the alaphabet.")
    else:
        print(response)
        incorrect_input = False


# response = [natobet[letter] for letter in word]
# print(response)
