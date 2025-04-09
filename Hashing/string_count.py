# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

if __name__ == "__main__":
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]


def countConsistentStrings(allowed , words):
    count = 0
    for word in words:
        for char in word:
            if char in allowed:
                char_present = True
            else:
                char_present = False
                break
        if char_present == True:
            count = count+1
    print(count)
countConsistentStrings(allowed , words)