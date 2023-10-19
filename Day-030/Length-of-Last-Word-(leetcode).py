class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split()
        x = t[len(t)-1]
        return len(x)
