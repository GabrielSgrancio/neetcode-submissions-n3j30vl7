class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range (1, len(s)):
            value = abs(ord(s[i]) - ord(s[i-1]))
            total += value  
        return total
            