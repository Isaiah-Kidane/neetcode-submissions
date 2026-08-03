class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        stack = []
        fleets = 0
        cars = sorted(zip(position,speed), reverse =True)
    
        for i,j in cars:
            if not stack:
                stack.append((target-i) / j)
                fleets += 1
                continue
            if (target - i) / j <= stack[-1]:
                continue
            else:
                stack.append((target-i) / j)
                fleets += 1
            
        return fleets
