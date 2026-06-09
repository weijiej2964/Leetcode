class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer question
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            cur = numbers[index1] + numbers[index2]
            if cur == target:
                return [index1 + 1, index2 + 1]
            elif cur > target:
                index2 -= 1
            else:
                index1 += 1


        return [index1 + 1, index2 + 1]