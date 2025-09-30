class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans, place = [], []

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r + c >= len(place):
                    place.append([])
                place[r+c].append(mat[r][c])

        for i in range(len(place)):
            if i % 2 == 0:
                place[i].reverse()
            for j in place[i]:
                ans.append(j)

        return ans
