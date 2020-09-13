class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        for i in nums:
            if i < res:
                return i
        return res