class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            # pair and sort by position descending (front of highway first)
        cars = sorted(zip(position, speed), reverse=True)
    
        stack = []  # holds arrival times of confirmed fleets
    
        for pos, spd in cars:
            time = (target - pos) / spd
        
        # only a strictly greater time means a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        # otherwise, this car merges into the fleet ahead — do nothing
    
        return len(stack)