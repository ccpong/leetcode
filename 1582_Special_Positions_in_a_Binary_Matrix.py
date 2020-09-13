class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def sp(mat,n,m):
            if mat[n].count(1)==1 and [mat[i][m] for i in range(len(mat))].count(1)==1:
                return 1
            return 0
        
        if not mat: return 0
        res=0
        for n in range(len(mat)):
            for m in range(len(mat[0])):
                if mat[n][m]==1:
                    res+=sp(mat,n,m)
        return res