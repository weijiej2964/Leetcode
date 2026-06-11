class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0

        an, l, r = 1,0, 1
        window = set(s[l])
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
            else:
                window.remove(s[l])
                l += 1
            an = max(len(window), an)
        return an

            

