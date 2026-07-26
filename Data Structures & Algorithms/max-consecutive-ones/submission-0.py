class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, res = 0, 0
        for num in nums:
            if num == 1:
                counter += 1
                res = max(res, counter)
            else:
                counter = 0
        return max(res, counter)
