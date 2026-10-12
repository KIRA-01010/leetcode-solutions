# Problem: Palindrome Number
# Difficulty: Easy

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original_x = x
        reverse_x = 0

        while x > 0:
            reverse_x = reverse_x * 10 + x % 10
            x //= 10

        return reverse_x == original_x