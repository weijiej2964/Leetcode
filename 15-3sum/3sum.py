class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # can't sort, mess up order
        # do two pointers w/ a hashmap for third number
        an = []
        nums.sort()

        seen = set()

        for i, a in enumerate(nums):
            if a in seen:
                continue
            seen.add(a)
            l = i + 1
            r = len(nums) - 1
            while l < r and not (l >= len(nums) and r <= i):
                if nums[l] + nums[r] + a == 0:
                    an.append([a, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1] :
                        l += 1
                elif nums[l] + nums[r] + a > 0:
                    r -= 1
                else:
                    l += 1
        
        return an

       


        


        