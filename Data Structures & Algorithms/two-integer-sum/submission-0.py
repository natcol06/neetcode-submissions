class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        assert len(nums) >= 2
        assert len(nums) <= 1000

        stored = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in stored:
                return [stored[difference], i]
            stored[num] = i
                

        return []
        
