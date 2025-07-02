class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #pair of number and min num left, mono decreasing 
        curMin = nums[0] #stored 1st element

        for n in nums[1:]: #skipped ele 1 its already in currMin
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]: #got our 132
                return True
            
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False