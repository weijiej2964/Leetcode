class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force
        an, l, r = 0, 0, len(height)-1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            if area > an:
                an = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return an

