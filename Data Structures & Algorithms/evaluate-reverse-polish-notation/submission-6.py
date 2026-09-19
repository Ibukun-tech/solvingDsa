class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c  not in "+,-,*,/":
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                r = 0
                if   c == '+': r = b + a
                elif c == '-': r = b - a
                elif c == '*': r = b * a
            # truncate toward zero
                else:          r = int(b / a)
                stack.append(r)
        return stack[-1]
