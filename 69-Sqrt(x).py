class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x
        if x == 0:
            return 0
        while guess*guess > x:
            guess = (guess+x// guess) // 2 

        return guess
        
