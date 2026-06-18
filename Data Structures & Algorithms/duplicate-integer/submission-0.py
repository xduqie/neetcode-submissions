class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t=[]
        for i in nums:
            if i not in t:
                t.append(i)
            else:
                return True
        return False


        