class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        an = 0
        num_to_count = {}
        for i in nums:
            num_to_count[i] = 0
        
        def fillLongestConsecutiveFor(key):
            if key-1 not in num_to_count:
                num_to_count[key] = 1
                return
            if num_to_count[key-1] == 0:
                fillLongestConsecutiveFor(key-1)
            num_to_count[key] = num_to_count[key-1] + 1


        for key in num_to_count.keys():
            if num_to_count[key] == 0:
                fillLongestConsecutiveFor(key)
                if an < num_to_count[key]:
                    an = num_to_count[key]
        

        return an
