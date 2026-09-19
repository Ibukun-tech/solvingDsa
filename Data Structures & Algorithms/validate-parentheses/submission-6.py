class Solution:
    def isValid(self, s: str) -> bool:
        pairs=  {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False
        
        return len(stack) == 0