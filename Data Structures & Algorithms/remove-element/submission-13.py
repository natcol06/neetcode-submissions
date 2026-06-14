class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums)          # one past the last live element
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]   # pull a candidate from the end
                right -= 1                      # shrink the unprocessed region
                # note: left does NOT advance — the swapped-in value is unchecked
            else:
                left += 1
        return left