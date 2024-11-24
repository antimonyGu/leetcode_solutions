class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToStart = {}

        for idx, num in enumerate(nums):
            if num not in numToStart:
                numToStart[num] = idx
            else:
                if (idx - numToStart[num]) <= k:
                    return True
                numToStart[num] = idx

        return False