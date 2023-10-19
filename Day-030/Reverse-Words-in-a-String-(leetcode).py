class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp.reverse()
        s = ""
      
        for i in range(0, len(temp)):
            s = s + temp[i] + " "
        return(s[:len(s)-1])
