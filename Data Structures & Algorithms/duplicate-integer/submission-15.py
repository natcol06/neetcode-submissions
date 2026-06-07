class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checked_list = set()

        if len(nums) <= 1:
            return False

        if len(nums) <= 10**5:
            pass
        else:
            return False

        for i in range(len(nums)):
            current = nums[i]
            if current in checked_list:
                return True
            checked_list.add(current)

        return False