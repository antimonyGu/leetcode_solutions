class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_i = sorted(intervals)

        res = [sorted_i[0]]

        for i in range(1, len(sorted_i)):
            if (res[-1][1] >= sorted_i[i][0]):
                res[-1][1] = max(res[-1][1], sorted_i[i][1])
            else:
                res.append(sorted_i[i])
        
        return res