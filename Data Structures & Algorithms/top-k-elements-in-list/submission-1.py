from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = Counter(nums)
        data = common.most_common(k)
        return [num for num, count in data]