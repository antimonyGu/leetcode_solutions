class Solution:
    def removeDuplicates(self, s: str) -> str:
        # two pointers
        end, a = -1, list(s)
        for c in a:
            if end >= 0 and a[end] == c:
                end -= 1
            else:
                end += 1
                a[end] = c
        return ''.join(a[: end + 1])


    def stackSolution(self, s: str) -> str:
        stack = []

        for char in s:
            if (len(stack) > 0 and stack[-1] == char):
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)