class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = ""
        for t in s:
            val = ord(t)  
            binary += format(val, "08b")
        return binary == binary[ : : -1]