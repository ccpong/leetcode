class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        maxL,currentL = 1,1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                if len(set(s[i-currentL:i+1]))==currentL+1:
                    currentL+=1
            maxL=max(maxL,currentL)
        return maxL