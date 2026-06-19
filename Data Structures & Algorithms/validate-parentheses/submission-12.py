class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_to_close = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        
        for char in s:
            if char in open_to_close:
                stack.append(open_to_close[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        
        return not stack
            