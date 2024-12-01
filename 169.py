class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.hashmapSolution(nums)
    
    # Time: O(N)
    # Space: O(N)
    def hashmapSolution(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
    # Time: O(N)
    # Space: O(1)
    def boyermooreSolution(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate