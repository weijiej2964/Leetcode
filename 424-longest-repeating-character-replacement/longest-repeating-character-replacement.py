class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = defaultdict(int)
        l, r = 0, 0 #size = r - l + 1
        while r < len(s):
            window[s[r]] += 1
            mostfreqchar = s[0]
            for i, a in window.items():
                if a > window[mostfreqchar]:
                    mostfreqchar = i
            windowsize = r - l + 1
            k_used = windowsize - window[mostfreqchar]
            while k_used > k:
                window[s[l]] -= 1
                l += 1
                mostfreqchar = s[0]
                for i, a in window.items():
                    if a > window[mostfreqchar]:
                        mostfreqchar = i
                windowsize = r - l + 1
                k_used = windowsize - window[mostfreqchar]
            r += 1
            res = max(res,windowsize)


        
        return res



        
                 