class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        arr = [0] * ((len(s)//2) + 1)

        level = -1
        ans = 0

        for i in range(len(s)):
            
            if s[i] == ")":
                if arr[level+1] == 0:
                    arr[level] += 1
                else:
                    arr[level] += arr[level+1] * 2
                    arr[level+1] = 0

                if level == 0:
                    ans += arr[level]
                    arr[level] = 0

                level -= 1

            else:
                level += 1

        return ans 
