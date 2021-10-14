import pandas

# importing data from csv
alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# changing data from DataFrame to dictionary
alphabet_dict = {row.letter: row.code for (
    index, row) in alphabet_data_frame.iterrows()}

# asking user for input
user_input = input("Enter a word: ").upper()


# looking for word inside dictionary for each letter from user input
NATO_alphapet_for_word = [alphabet_dict[letter] for letter in user_input]


# printing result
for word in NATO_alphapet_for_word:
    print(word, end='')
    if word != NATO_alphapet_for_word[-1]:
        print(', ', end='')
