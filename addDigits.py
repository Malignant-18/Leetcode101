#   PROBLEM STATEMENT - #258
#   method adopted   - RECURSION
#   time complexity  - O(logn)
#   space complexity - O(logn)

class Solution(object):
    def addDigits(self, num):
        if (num <10):
            return num
        return self.addDigits(num//10+num%10)
 