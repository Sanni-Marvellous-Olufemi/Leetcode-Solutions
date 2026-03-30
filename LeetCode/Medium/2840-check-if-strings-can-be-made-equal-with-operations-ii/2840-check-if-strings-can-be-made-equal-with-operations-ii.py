class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        one = defaultdict(int)
        two = defaultdict(int)
        three = defaultdict(int)
        four = defaultdict(int)

        for i in range(len(s1)):
            if i % 2 == 0:
                one[s1[i]] += 1
                two[s2[i]] += 1
            else:
                three[s1[i]] += 1
                four[s2[i]] += 1

        return one == two and three == four

        

