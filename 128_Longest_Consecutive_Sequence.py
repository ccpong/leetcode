class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums=sorted(set(nums))
        ans=1
        last=nums[0]
        cur=1
        for i in range(len(nums)):
            if nums[i]==last+1:
                cur+=1
                ans=max(cur,ans)
            else:
                cur=1
            last=nums[i]
        return ans