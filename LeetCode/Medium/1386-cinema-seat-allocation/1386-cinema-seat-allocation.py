class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        j = 0
        ans = 0
        seats = [{2, 3, 4, 5}, {4, 5, 6, 7}, {6, 7, 8, 9}]
        curr = [1, 1, 1]
        start = reservedSeats[0][0]
        count = 1

        while j < len(reservedSeats):
            if reservedSeats[j][0] != start:
                total = sum(curr)
                ans += (total - 1) if (total > 1 and curr[1] == 1) else total
                start = reservedSeats[j][0]
                count += 1
                curr[0], curr[1], curr[2] = 1, 1, 1

            num = reservedSeats[j][1]

            for k in range(3):
                if num in seats[k]:
                    curr[k] = 0

            j += 1

        total = sum(curr)
        ans += (total - 1) if (total > 1 and curr[1] == 1) else total
        ans += (n - count) * 2
            
        return ans      