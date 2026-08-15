class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for x in nums:
            if x in vistos:
                return True
            vistos.add(x)
        return False
        