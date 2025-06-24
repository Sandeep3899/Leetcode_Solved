class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Win_sum = sum(nums[:k])
        Max_sum = Win_sum

        for i in range(k, len(nums)):
            Win_sum += nums[i] - nums[i-k]
            Max_sum = max(Max_sum, Win_sum)
        return Max_sum/k

        