class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        length, width, dia, area = 0, 0, 0, 0

        for l, w in dimensions:
            d = math.sqrt((l*l)+(w*w))
            a = l * w

            if d > dia:
                length, width, dia, area = l, w, d, a
            elif d == dia and a > area:
                length, width, area = l, w, a

        return area