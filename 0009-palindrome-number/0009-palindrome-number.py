class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert the number to a string and compare with its reverse
        s = str(x)
        return s == s[::-1]