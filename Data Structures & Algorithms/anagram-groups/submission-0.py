class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strss = sorted(strs)
        output = {}
        for i in strss:
            key = tuple(sorted(i))
            if key not in output:
                output[key]=[]
            output[key].append(i)
        return list(output.values())
                