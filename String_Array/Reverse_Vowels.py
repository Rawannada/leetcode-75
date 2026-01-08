class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        my_vowels = []
        indices = []
        vowels = "aeiouAEIOU"
        for i in range (len(s)):
            if s[i] in vowels:
                my_vowels.append(s[i])
                indices.append(i)
        my_vowels.reverse()
        for i in range (len(my_vowels)):
            s[indices[i]] = my_vowels[i]
        return "".join(s)

