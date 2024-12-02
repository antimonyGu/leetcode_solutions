class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd length palindrom case
            l = r = i
            res += self.countPalidrome(s, l, r)

            l = i
            r = i + 1
            res += self.countPalidrome(s, l, r)

        return res
    
    def countPalidrome(self, s, l, r) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            # move prointers
            l -= 1
            r += 1
        
        return count