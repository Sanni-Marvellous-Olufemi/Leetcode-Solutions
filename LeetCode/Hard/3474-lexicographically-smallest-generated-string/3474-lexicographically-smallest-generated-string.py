class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = [0 for i in range(n+m-1)]
        sets = set()

        for i in range(n):
            k = i

            if str1[i] == "T":
                j = 0

                while j < m:
                    if ans[k] != 0 and str2[j] != ans[k]:
                        return ""
                    ans[k] = str2[j]
                    sets.add(k)
                    j += 1
                    k += 1

            else:
                if ans[k] != 0 and ans[k] == str2:
                    return ""

                if ans[k] == 0:
                    if str2 != "a":
                        ans[k] = "a"
                    else:
                        ans[k] = "b"


        if str1[-1] == "F" and k < len(ans):
            for i in range(n, len(ans)):
                ans[i] = "a" if ans[i] == 0 else ans[i]

            ans[-1] = "b" if set(str1) == {"a"} else ans[-1]


        for i in range(n):
            if str1[i] == 'F' and "".join(ans[i : i + m]) == str2:
                changed = False

                for j in range(m - 1, -1, -1):
                    idx = i + j
                    if idx not in sets:
                        ans[idx] = 'b' if ans[idx] == 'a' else 'a'
                        changed = True
                        break
                if not changed:
                    return ""

        return "".join(ans)
