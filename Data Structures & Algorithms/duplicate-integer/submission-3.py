# [1, 2, 3, 1]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for n in nums:
            if n in hash:
                return True
            else:
                hash.add(n)
        return False

