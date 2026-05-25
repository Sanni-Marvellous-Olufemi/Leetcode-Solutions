class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        end = minJump

        while queue:
            node = queue.popleft()
            start = max(node+minJump, end)
            end = min(node+maxJump+1, len(s))
            
            for i in range(start, end):
                if s[i] == "0":
                    if i == len(s)-1:
                        return True
                    queue.append(i)
            
            if end == len(s):
                break

        return False
