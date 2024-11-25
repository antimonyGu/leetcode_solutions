class Solution:
    def myAtoi(self, s: str) -> int:
        num = '0123456789'
        res = ''

        for x in s:
            # skip leading space
            if x == ' ' and len(res) == 0:
                continue
            
            # handle first character
            if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
                res += x
            # handle number
            elif x in num:
                res += x
            else:
                break
        
        if res == '' or res in '-+':
            return 0

        resNum = int(res)
        if resNum < -(2**31):
            return -(2**31)
        elif resNum > (2**31 - 1):
            return (2**31 - 1)
        else:
            return resNum
