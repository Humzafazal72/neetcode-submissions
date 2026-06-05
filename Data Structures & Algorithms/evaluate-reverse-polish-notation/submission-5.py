class Solution:
    def isnum(self, token):
        try:
            num = int(token)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isnum(token):
                stack.append(int(token))
            elif token=='+':
                top1, top2 = stack.pop(), stack.pop()
                stack.append(top1+top2)
            elif token=='-':
                top1, top2 = stack.pop(), stack.pop()
                stack.append(top2-top1)
            elif token=='/':
                top1, top2 = stack.pop(), stack.pop()
                stack.append(int(top2/top1))
            else:
                top1, top2 = stack.pop(), stack.pop()
                stack.append(top1*top2)
        return stack.pop()