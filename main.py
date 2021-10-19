import pandas

# importing data from csv
alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# changing data from DataFrame to dictionary
alphabet_dict = {row.letter: row.code for (
    index, row) in alphabet_data_frame.iterrows()}


wrong_word_format = True
while wrong_word_format:
    # asking user for input
    user_input = input("Enter a word: ").upper()
    try:
        # looking for word inside dictionary for each letter from user input
        NATO_alphapet_for_word = [alphabet_dict[letter]
                                  for letter in user_input]
    # if user entered wrong formated word
    except KeyError:
        print("Sorry only letters in one word are alowed")
    else:
        wrong_word_format = False

# printing result
for index, word in enumerate(NATO_alphapet_for_word):
    print(word, end='')
    if index != len(NATO_alphapet_for_word) - 1:
        print(', ', end='')
