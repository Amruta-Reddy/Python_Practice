import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in file.iterrows()}

user_word = input("Enter a Word: ").upper()

final_list = [new_dict[letter] for letter in user_word]

print(final_list)
