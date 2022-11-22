class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        
        string = haystack[left:right]
        if string == needle:
            return 0
        
        else:
            for i in range(len(needle), len(haystack)):
                string = string[1:] + haystack[i]
                left+=1
                if string == needle:
                    return left
                print(string)
            return -1
            