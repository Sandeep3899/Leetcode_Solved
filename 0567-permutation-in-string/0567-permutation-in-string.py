class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = {}
        windowCount = {}
        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            windowCount[s2[i]] = 1 + windowCount.get(s2[i], 0)

        if countS1 == windowCount:
            return True
        
        for i in range(len(s1), len(s2)):
            l = s2[i-len(s1)]
            r = s2[i]

            windowCount[r] = 1 + windowCount.get(r, 0)

            windowCount[l] -= 1
            if windowCount[l] == 0:
                del windowCount[l]

            if countS1 == windowCount:
                return True
        return False 
            