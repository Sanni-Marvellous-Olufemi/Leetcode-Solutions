class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x = y = di = 0
        obstacle_set = set(map(tuple, obstacles))
        max_sq_dist = 0
        
        for cmd in commands:
            if cmd == -2:  
                di = (di - 1) % 4
            elif cmd == -1:  
                di = (di + 1) % 4
            else:  
                for _ in range(cmd):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_sq_dist = max(max_sq_dist, x*x + y*y)
                    else:
                        break
                        
        return max_sq_dist