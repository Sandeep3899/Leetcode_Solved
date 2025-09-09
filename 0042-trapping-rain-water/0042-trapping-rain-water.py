class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        Lmax, Rmax = height[l], height[r]
        res = 0

        while l < r:
            if Lmax < Rmax:
                l += 1
                Lmax = max(Lmax, height[l])
                res += Lmax - height[l]
            else:
                r -= 1
                Rmax = max(Rmax, height[r])
                res += Rmax - height[r]
        return res
        

        