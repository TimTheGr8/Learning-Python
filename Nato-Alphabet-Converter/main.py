import pandas

alpha_data = pandas.read_csv("Nato-Alphabet-Converter/nato_phonetic_alphabet.csv")
natobet = {row.letter: row.code for (index, row) in alpha_data.iterrows()}

word = input("Enter a word: ").upper()

response = [natobet[letter] for letter in word]
print(response)
