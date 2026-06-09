class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        running_prefix = 1
        for i in range(n):
            output[i] = running_prefix
            running_prefix *= nums[i]

        running_suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= running_suffix
            running_suffix *= nums[i]

        return output