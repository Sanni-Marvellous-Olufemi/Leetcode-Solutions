class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        hashmap = {}
        ans = 0
        hashmap["row"] = set()
        hashmap["col"] = set()
        hashmap["dia"] = set()
        hashmap["anti"] = set()

        def walk(r, c, queens):
            nonlocal n, ans

            if c == n:
                r += 1
                c = 0

            if r >= n:
                if queens == n:
                    ans += 1
                return

            if (c not in hashmap["col"]) and (r not in hashmap["row"]) and (r-c not in hashmap["dia"]) and (r+c not in hashmap["anti"]):

                hashmap["col"].add(c)
                hashmap["row"].add(r)
                hashmap["dia"].add(r-c)
                hashmap["anti"].add(r+c)

                walk(r, c+1, queens+1)
                
                hashmap["col"].remove(c)
                hashmap["row"].remove(r)
                hashmap["dia"].remove(r-c)
                hashmap["anti"].remove(r+c)

            walk(r, c+1, queens)


        walk(0, 0, 0)
        return ans