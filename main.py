import pandas

# df is going to be our dataframe.
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# using dictionary comprehension to iterate the rows
NATO_phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# each of the word in NATO phonetic alphabet is an upper case
capital_word = input("please enter a word: ").upper()

# create a list comprehension of the phonetic code words from a word that the user inputs.
list_of_phonetic_code = [NATO_phonetic_dict[letter] for letter in capital_word]
print(list_of_phonetic_code)
