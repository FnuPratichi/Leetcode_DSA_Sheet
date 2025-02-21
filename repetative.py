# An isogram is a word that has no duplicate letters. Create a function that takes a
# string and returns either True or False depending on whether or not it's an "isogram".
# Examples : is_isogram("Algorism") ➞ True
# is_isogram("PasSword") ➞ False
# - Not case sensitive.
# is_isogram("Consecutive") ➞ False
# Notes : Ignore letter case (should not be case sensitive).
# All test cases contain valid one word strings.

def check_duplicates(word):
    word = word.lower()
    ans = True
    my_dict = {}
    for letter in word:
        if letter in my_dict:
            my_dict[letter] = my_dict[letter]+1
        else:
            my_dict[letter] = 1

    for values in my_dict.values():
        if values>1:
            ans = False

    if ans is True:
        print('true')
    else:
        print('false')

check_duplicates('Consecutive')
check_duplicates('PasSword')
check_duplicates('Algorism')