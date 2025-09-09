class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if nums[i-1] == a and i > 0:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum>0:
                    r -= 1
                elif threeSum<0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l = l + 1
                    while nums[l - 1] == nums[l] and l<r:
                        l += 1
        return res