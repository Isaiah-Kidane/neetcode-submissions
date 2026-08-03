class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = 0

        while l < r:
            bot = min(heights[l],heights[r])
            area = bot * (r-l)
            if area > maxi:
                maxi = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l +=1
        return maxi