class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        an = 0
        mySet = set() 
        for num in nums:
            mySet.add(num)
        
        for i in mySet:
            if i - 1 in mySet:
                continue
            count = i + 1
            while count in mySet:
                count += 1
            if count - i > an:
                an = count - i
        
        return an
