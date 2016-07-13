class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = str(x)
        for i in range(len(num)/2):
            if num[i] !=num[len(num) - i -1]:
                return False
        return True