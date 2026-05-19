class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Acts as our memory bank
        
        for i, v in enumerate(nums):
            check = target - v
            
            # Did we already pass the number we need?
            if check in seen:
                return [seen[check], i]
                
            # If not, remember the current number and its index
            seen[v] = i
