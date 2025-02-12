class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = []
        for i in word1:
            for j in word2:
                if len(word1)==len(word2):
                    merged_word.append(2*i)
                    i = i+1
                    merged_word.append(j+1)
                    j=j+1
                

        