class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[]
        n=len(word1)
        m=len(word2)
        for i in range(n+1):
            dp.append([])
            for j in range(m+1):
                if i==0 or j==0:
                    dp[-1].append(max(i,j))
                elif word1[i-1]==word2[j-1]:
                    dp[-1].append(dp[i-1][j-1])
                else:
                    case1=dp[i-1][j-1]+1
                    case2=dp[i][j-1]+1
                    case3=dp[i-1][j]+1
                    dp[-1].append(min(case1,case2,case3))
        return dp[-1][-1]