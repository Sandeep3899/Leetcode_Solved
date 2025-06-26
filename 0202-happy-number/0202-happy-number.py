class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(number: int) -> int:
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit * digit
                number //= 10
            return total_sum
        slow = n
        fast = nextNum(n)

        while fast != 1 and slow != fast:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
        return fast == 1