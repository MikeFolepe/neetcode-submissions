class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_count=dict(sorted(count.items(), key=lambda item: item[1]))
        res = []
        while k > 0:
            res.append(sorted_count.popitem()[0])
            k -= 1
        
        return res
