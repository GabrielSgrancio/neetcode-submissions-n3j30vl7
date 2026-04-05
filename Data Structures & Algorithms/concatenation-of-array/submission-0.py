class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #receive array nums lenght n
        #create new array ans length 2n
        #ans[i] == nums[i] //1st elemen ==
        #ans[i+n] == nums[i] //

        #pretty much duplicate nums arr
        ans = []
        for i in range(0, 2):
            for j in range(len(nums)):
                ans += [nums[j]]
        return ans