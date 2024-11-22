class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        diagonalDict = defaultdict(list)
        # key - diagonal elements have the same r + c value
        for r in range(R):
            for c in range(C):
                diagonalDict[r + c].append(mat[r][c])

        ans = []
        # ifs c + r is odd append to ans sequential, else reverse append to ans:
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        
        return ans

