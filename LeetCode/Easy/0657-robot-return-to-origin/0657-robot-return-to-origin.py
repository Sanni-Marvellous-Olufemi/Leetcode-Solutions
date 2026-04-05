class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hashmap = {"U":0, "D":0, "L":0, "R":0}

        for i in moves:
            hashmap[i] += 1

        return hashmap["U"] == hashmap["D"] and hashmap["L"] == hashmap["R"]