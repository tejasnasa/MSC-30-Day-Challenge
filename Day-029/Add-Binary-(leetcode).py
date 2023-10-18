class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aint = 0
        bint = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while (i >= 0):
            aint += int(a[i]) * (2 ** (len(a) - i - 1))
            i -= 1
        while (j >= 0):
            bint += int(b[j]) * (2 ** (len(b) - j - 1))
            j -= 1

        return bin(aint + bint)[2:]
