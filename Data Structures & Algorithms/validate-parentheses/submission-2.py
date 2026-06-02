class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {']':'[',')':'(','}':'{'}
        for prn in s:
            if prn in ['[','(','{']:
                stack.append(prn)
                continue
            if not stack:
                return False
            top = stack.pop()
            if top != match[prn]:
                return False
        if stack:
            return False
        return True