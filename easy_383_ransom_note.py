"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        for char in magazine:
            if(char in d1):
                d1[char]=d1[char]+1
            else:
                d1[char]=1
        
        d2={}
        for char in ransomNote:
            if(char in d2):
                d2[char]=d2[char]+1
            else:
                d2[char]=1

        for key in d2:
            if key not in d1: #Quella lettera non compare nella magazine
                return False
            elif d1[key]<d2[key]:#Non ci sono abbastanza lettere nella magazine
                return False
        return True

sol=Solution()
print(sol.canConstruct("baaaacbc","aaabbcccddaac"))