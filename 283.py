# Time: O(n)
# Space: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                # swap fast and slow's element
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            if nums[slow] != 0:
                slow += 1