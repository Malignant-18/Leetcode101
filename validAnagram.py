#   PROBLEM STATEMENT - 242
#   method adopted  - SORTING
#   time complexity  - O(nlogn)
#   space complexity - O(n)

class Solution(object):
    def isAnagram(self, s, t):
        return ''.join(sorted(s)) == ''.join(sorted(t))
    