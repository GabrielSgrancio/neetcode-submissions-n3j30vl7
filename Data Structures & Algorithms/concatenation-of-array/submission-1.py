class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        response = nums[:]
        for i in nums:
            response.append(i)
        return response