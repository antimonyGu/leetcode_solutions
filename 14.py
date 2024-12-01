class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge cases
        if len(strs) == 0:
            return ""

        ans = ""
        shortest = min(strs, key=len)
        # enumerate shortest str's length
        for i in range(len(shortest)):
            # check every char in the strs
            for j in range(len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    return ans
            
            ans += strs[0][i]
        
        return ans