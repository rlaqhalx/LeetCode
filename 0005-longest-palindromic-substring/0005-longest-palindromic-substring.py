class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    left = left - 1
                    right = right + 1
                else:
                    break
            
            # [include: exclude]
            # left and right is out of bound or reached Not palindrome part
            # so need to bring each boundary to one step closer
            # since [include: exclude], you need to add + 1 to left side 
            # and do nothing for right as it does -1 automatically by excluding
            return s[left + 1: right]

        longest = ""
        for i in range(len(s)):
            # odd (center is i,i)
            sub1 = expand(s, i, i)
            if len(sub1) > len(longest):
                longest = sub1
            # even (center is i, i+1 (between i and i+1))
            sub2 = expand(s, i, i+1)
            if len(sub2) > len(longest):
                longest = sub2
        
        return longest