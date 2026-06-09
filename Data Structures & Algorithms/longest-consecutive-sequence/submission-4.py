class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
    
        max_length = 0

    # Step 2: Loop through every number
        for num in nums:
        # Step 3: Check if it's a sequence start
            if (num - 1) not in num_set:
                current = num
                length = 1

            # Step 5: Count forward while chain exists
                while (current + 1) in num_set:
                    current += 1
                    length += 1

            # Step 6: Track the maximum
                max_length = max(max_length, length)

        return max_length