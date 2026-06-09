class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[k]=nums[j]
                k+=1
        for j in range(k, len(nums)):
            nums[j]=0