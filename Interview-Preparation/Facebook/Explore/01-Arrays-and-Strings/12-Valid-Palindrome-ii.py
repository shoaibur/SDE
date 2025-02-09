class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s):
            return s == s[::-1]
        
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s[i:j]) or isPalindrome(s[i+1:j+1])
            i, j = i+1, j-1
        return True
