class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        cars = [(pos,speed) for pos,speed in zip(position,speed)]
        cars.sort(reverse=True)
        stack = []

        for car in cars:
            steps = (target-car[0])/car[1]
            if not stack:
                stack.append(steps)
                continue

            if steps<=stack[-1]:
                continue
            else:
                stack = []
                fleet+=1
                stack.append(steps)
        
        return fleet+1
