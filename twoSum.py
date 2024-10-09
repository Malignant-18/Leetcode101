#   PROBLEM STATEMENT - 1
#   method adopted  - HASHMAP
#   time complexity  - O(n)
#   space complexity - O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i , num in enumerate (nums):
            complement = target - num
            if complement in map :
                return[map[complement] , i]
            map[num] = i
        
        return []