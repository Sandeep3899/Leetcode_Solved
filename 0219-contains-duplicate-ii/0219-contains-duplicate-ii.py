class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from typing import List


        index_map = {}  # store number -> last index
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # update last seen index
        
        return False
