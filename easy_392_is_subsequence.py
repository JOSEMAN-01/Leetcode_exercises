"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True #se la stringa è vuota...
        i=0 #lunghezza della più grande sottosequenza 
        for char in t:
            if(i<len(s)):
                if(char==s[i]):
                    i+=1

        return i==len(s)
    
sol=Solution()
print(sol.isSubsequence("b","abc"))