class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i in string.punctuation or i in " ":
                s = s.replace(i,"")
        s = s.lower()
        if (s == s[::-1]):
            return True
        return False
