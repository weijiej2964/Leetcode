class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = abs(nums[0])
        negateCount = 0
        zeroCount = 0
        if nums[0] < 0:
            negateCount = 1
        
        if nums[0] == 0:
            product = 1
            zeroCount = 1
    
        for n in range(1, len(nums)):
            if nums[n] < 0:
                negateCount += 1
        
            if nums[n] == 0:
                zeroCount += 1
            else:
                product *= abs(nums[n])
        
        print(product)

        res = [0 for i in range(len(nums))]

        for n in range(0, len(nums)):
            if zeroCount > 1:
                continue
            if zeroCount == 1 and nums[n] != 0:
                continue
            if nums[n] == 0:
                if negateCount % 2 == 1:
                    res[n] -= product
                else:
                    res[n] += product
            elif nums[n] > 0:
                if negateCount % 2 == 1:
                    res[n] -= int(product/nums[n])
                else:
                    res[n] += int(product/nums[n])
            else:
                if (negateCount - 1) % 2 == 1:
                    res[n] -= int(product/abs(nums[n]))
                else:
                    res[n] += int(product/abs(nums[n]))
            
        return res


    

        