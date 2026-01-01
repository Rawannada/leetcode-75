class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                r =r + word1[i]
            if i < len(word2):
                r = r + word2[i]
            i =i+ 1

        return r