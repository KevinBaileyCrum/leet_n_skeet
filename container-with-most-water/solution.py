class Solution:
    def maxArea(self, height: List[int]) -> int:
        pHead = 0
        pTail = len(height)-1
        maxVol = 0
        while (pHead != pTail):
            currVol = min(height[pHead], height[pTail]) * (pTail - pHead)
            if (currVol > maxVol):
                maxVol = currVol
            if (height[pHead] < height[pTail]):
                pHead += 1
            else:
                pTail -=1
        return maxVol

