class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        result = []
    
        while r < len(nums):
            # Scan the sub-array to find the max
            current_max = max(nums[l:r+1]) 
            result.append(current_max)
        
            # Move the window forward
            l += 1
            r += 1
        
        return result