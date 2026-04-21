class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = 0
        
        while n < len(nums):
            res = 1
            for idx,val in enumerate(nums):
                if idx == n:
                    continue
                res *= val
            output.append(res)
            n += 1
        return output
            


