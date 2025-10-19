class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        sets, queue, ans = set(), deque(), s
        queue.append(s)

        while queue:
            s = queue.popleft()

            if s not in sets:
                rot = s[len(s)-b:] + s[:len(s)-b]
                add = ""

                for i in range(len(s)):
                    if i % 2 == 1:
                        add += str((int(s[i]) + a) % 10)
                    else:
                        add += s[i]
                
                ans = min(ans, add, rot)
                queue.append(rot)
                queue.append(add)
                sets.add(s)

        return ans

            


        





"""
{1,3,7,9} = 0
{0,2,4,6,8} = a % 2
{5} = a % 5

"""