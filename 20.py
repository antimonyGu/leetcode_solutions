class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end2Start = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for i, char in enumerate(s):
            if char in end2Start.values():
                stack.append(char)
            else:
                if (len(stack) > 0 and stack[-1] == end2Start[char]):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
