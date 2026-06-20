class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gng = {}
        
        for i, n in enumerate(nums):
            diff=(target-n)

            if diff in gng:
                return [gng[diff], i]
            gng[n] = i
        return []