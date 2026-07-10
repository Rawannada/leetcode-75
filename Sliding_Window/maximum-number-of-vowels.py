class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a" ,"e","i","o","u"}
        max_sum = 0
        for vowel in range(k):
                if s[vowel] in vowels:
                    max_sum +=1


        ssum = max_sum
        z = 0
        while z < len(s)-k:
            if s[z] in vowels :
                ssum -=1
            if s[z+k] in vowels :
                ssum +=1
            max_sum = max(ssum,max_sum)
            z+=1
        
        return max_sum
