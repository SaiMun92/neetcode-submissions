class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for v in nums:
            if v not in hashmap:
                hashmap[v] = 1
            else:
                return True
        return False
         