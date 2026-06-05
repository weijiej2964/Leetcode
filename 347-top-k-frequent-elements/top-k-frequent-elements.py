class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Find num to freq pairs
        #plugs num into freq = index of count
        #reverse loop count until k nums found

        res = []
        remaining_k = k
        numAndFreq = defaultdict(int)
        count = [[] for i in range(len(nums) + 1)]
        for n in nums:
            numAndFreq[n] += 1
        
        for num, freq in numAndFreq.items():
            count[freq].append(num)
        
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                remaining_k -= 1
                if remaining_k == 0:
                    return res
        return res
