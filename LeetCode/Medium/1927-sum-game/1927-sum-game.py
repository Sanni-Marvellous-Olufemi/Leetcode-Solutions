class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        a,b = [0,0], [0,0]
        start, end = 0, 0
        alice = True
        # bob needs to have below alice before mid

        for i in range(len(num)):
            if num[i] == "?":
                if alice:
                    if i < mid:
                        a[0] += 1
                    else:
                        a[1] += 1
                    alice = False
                else:
                    if i < mid:
                        b[0] += 1
                    else:
                        b[1] += 1
                    alice = True

            else:
                if i < mid:
                    start += int(num[i])
                else:
                    end += int(num[i])

        a[0], a[1], b[0], b[1] = a[0] * 9, a[1] * 9, b[0] * 9, b[1] * 9

        if sum(a) + sum(b) == 0:
            return start != end

        if (start + a[0] > end + b[1]) or (end + a[1] > start + b[0]) or (end > start + b[0]) or (start > end + b[1]):
            return True
        
        return False
