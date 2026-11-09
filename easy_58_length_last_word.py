"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal consisting of non-space characters only.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        #optimal Pythonic solution
        return len(s.split()[-1])
        
        """
        My solution...
        
        r=s.split(" ")
        r=[item for item in r if item!=""]
        lastWord=r[len(r)-1]
        
        return len(lastWord)
        """