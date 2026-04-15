class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements_dict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            elements_dict[num] = 1 + elements_dict.get(num, 0)
        for num, counter in elements_dict.items():
            freq[counter].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res