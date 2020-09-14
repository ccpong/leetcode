class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Pal(s):
            return str(s)==str(s)[::-1]
        if len(s)==0: return s
        ans=s[0]
        for a in range(len(s)):
            for b in range(a+len(ans),len(s)+1):
                if Pal(s[a:b]):
                    if b-a>len(ans):
                        ans=s[a:b]
        return ans