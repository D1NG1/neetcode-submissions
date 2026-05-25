class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        m = 0

        while i<j:
            current = min(heights[i],heights[j]) *(j-i)
            m = max(m,current)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j -=1
        return m
