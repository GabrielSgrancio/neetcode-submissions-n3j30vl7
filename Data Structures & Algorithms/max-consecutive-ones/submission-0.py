class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        longest = 0

        for i in nums:
            if i == 1:
                counter += 1
                longest = max(longest, counter)
            else:
                counter = 0
        return longest