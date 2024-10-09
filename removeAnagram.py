#   PROBLEM STATEMENT - 1
#   method adopted  - SORTING
#   time complexity  - O(n m logm) where m is avg size of a word
#   space complexity - O(n)


class Solution(object):
    def anagram (self  , w ):
        return ''.join(sorted(w))
    def removeAnagrams(self, words):
        removed_list = [words[0]]
        for i in range(1 , len(words)):
            while (self.anagram(words[i]) != self.anagram(removed_list[-1])):
                removed_list.append(words[i])
        return removed_list