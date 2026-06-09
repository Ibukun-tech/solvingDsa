class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    
        left, right = 0, len(sorted_nums) - 1
    
        while left < right:
            i, a = sorted_nums[left]
            j, b = sorted_nums[right]
        
            current_sum = a + b
        
            if current_sum == target:
                return [min(i, j), max(i, j)]
            elif current_sum < target:
                left += 1
            else:
                right -= 1