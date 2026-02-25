class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        o = 0 
        limit = len(s)
        
        for i in range(len(t)):
            if o < limit and t[i] == s[o]:
                o = o + 1
        return o == limit