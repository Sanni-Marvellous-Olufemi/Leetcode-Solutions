class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        curr = []
        ans = []
        stack = []

        for i in range(len(healths)):
            curr.append([positions[i], i, healths[i], directions[i]])

        curr.sort()

        for i in curr:
            if i[-1] == "R":
                stack.append([i[1], i[2]])

            else:
                while stack:
                    if stack[-1][-1] < i[2]:
                        stack.pop()
                        i[2] -= 1

                    elif stack[-1][-1] == i[2]:
                        stack.pop()
                        i[2] = 0
                        break

                    else:
                        stack[-1][-1] -= 1
                        i[2] = 0
                        break

                if i[2] != 0:
                    ans.append([i[1], i[2]])

        ans += stack
        ans.sort()
        return [i[1] for i in ans]