class Solution:
    def findMin(self, nums: List[int]) -> int:
        #start binary search like normal
        #check if mid is in left(bigger) or right(smaller) section, (record mid in ans)
            #if mid is in left, then move l to m+1
            #if mid is in right, then move r to m-1
            #during this, always be checking if nums[l] < nums[r] --- since this means it is in sorted array
                #then we can just compare l with ans
        ans = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                return ans

            m = (l+r) // 2
            ans = min(ans,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans
            
                
