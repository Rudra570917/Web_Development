class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        return s == s[::-1]

#Leetcode 125. Valid Palindrome
#Problem Link: https://leetcode.com/problems/valid-palindrome/
#We can solve this problem by using two pointers, one starting from the beginning of the string and the other starting from the end. We will move the pointers towards each other while skipping non-alphanumeric characters and comparing the characters at the two pointers. If they are not equal, we return False. If we reach the middle of the string without finding any mismatches, we return True.