class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        if len(nums)==len(sets):
            return False
        else:
            return True 