# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(sentence):
    sent_set = set(sentence)
    if len(sent_set)==26:
        return True
    return False

checkIfPangram('thequickbrownfoxjumpsoverthelazydog')

# if __name__ == "__main__":
#     sentence = "thequickbrownfoxjumpsoverthelazydog"