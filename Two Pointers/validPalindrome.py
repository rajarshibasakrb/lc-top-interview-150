import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char not in string.punctuation])
        s = s.lower()
        s = "".join(s.split())
        
        if len(s) == 0 or len(s) == 1:
            return True

        l = 0
        r = len(s) - 1
        #Even length string
        if len(s) % 2 == 0: 
            while l < r :
                if s[l] != s[r]:
                    return False
                else:
                    l +=1 
                    r -= 1
        # Odd length string
        else: 
            while l != r:
                if s[l] != s[r]:
                    return False
                else:
                    l +=1 
                    r -= 1

        return True
