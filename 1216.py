class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def helper(beg, end, k):
            if k<0:
                return False
            if beg>=end:
                return True
            if s[beg]==s[end]:
                return helper(beg+1, end-1, k)
            else:
                return helper(beg, end-1, k-1) or helper(beg+1, end, k-1)
        return helper(0, len(s)-1, k)