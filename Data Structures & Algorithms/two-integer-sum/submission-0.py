class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for x in range(i,len(nums)):
            for y in range(i+1, len(nums)):
                if (nums[x]+nums[y]) == target:
                    out=[x,y]
                    return out
            i += 1