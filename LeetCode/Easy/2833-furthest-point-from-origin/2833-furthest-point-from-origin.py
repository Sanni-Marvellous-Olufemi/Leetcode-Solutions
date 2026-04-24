class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = Counter(moves)
        return abs(counter["R"] - counter["L"]) + counter["_"]