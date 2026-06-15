class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #start binary search as normal
        #check if rotated or not
        #we need to check if mid is in left or right half
            #if in left half & target >= l, then r = m-1
                # else l = m+1
            #if in right half & target < l, then l = m+1 
                #else r = m+1
        #not rotated = normal binary
        
        ans = -1
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            print(m)
            if nums[m] == target:
                return m
            if nums[l] <= nums[r]:
                #normal binary
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #rotated
                if nums[m] >= nums[l]:
                    #mid in left
                    if target >= nums[l]:
                        #target also in left
                        if target > nums[m]:
                            l = m+1
                        else:
                            r = m-1
                    else:
                        l = m+1
                else:
                    #mid in right
                    if target < nums[l]:
                        #target in right
                        if target > nums[m]:
                            l = m+1
                        else:
                            r = m-1
                    else:
                        r = m-1
                    
        return ans



