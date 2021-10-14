
import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


alphabet_dict = {}

for (index, row) in alphabet_data_frame.iterrows():
    alphabet_dict[row.letter] = row.code

user_input = input("Enter a word: ").upper()

NATO_alphapet_for_word = [alphabet_dict[letter] for letter in user_input]

for word in NATO_alphapet_for_word:
    print(word, end=', ')
