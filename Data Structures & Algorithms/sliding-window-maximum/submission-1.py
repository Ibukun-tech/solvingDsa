from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque() # Stores indices of elements
    
        for r in range(len(nums)):
        # 1. Remove elements from the back that are smaller than the current element
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            
        # 2. Add the current element's index to the back
            q.append(r)
        
        # 3. Calculate the left boundary of the current window
            l = r - k + 1
                # 4. Remove the front element if it's out of the window's left bound
            if q[0] < l:
                q.popleft()
            
        # 5. If the window has reached size k, the front of q is our max
            if r >= k - 1:
                result.append(nums[q[0]])
            
        return result
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # l = 0
        # r = k - 1
        # result = []
    
        # while r < len(nums):
        #     # Scan the sub-array to find the max
        #     current_max = max(nums[l:r+1]) 
        #     result.append(current_max)
        
        #     # Move the window forward
        #     l += 1
        #     r += 1
        
        # return result