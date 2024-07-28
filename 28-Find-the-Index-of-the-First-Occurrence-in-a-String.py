class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        hLen = len(haystack)
        nLen = len(needle)
        
        for i in range(hLen - nLen + 1):
            if haystack[i:i + nLen] == needle:
                return i
        
        return -1
