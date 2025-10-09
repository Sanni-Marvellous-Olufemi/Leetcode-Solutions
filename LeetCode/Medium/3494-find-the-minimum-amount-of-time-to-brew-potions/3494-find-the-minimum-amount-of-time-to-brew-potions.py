class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        f = [0] * len(skill)

        for i in mana:
            now = f[0]
            for j in range(1, len(skill)):
                now = max(now + skill[j-1]*i, f[j])

            f[-1] = now + (skill[-1] * i)
            for j in range(len(skill)-2, -1, -1):
                f[j] = f[j+1] - (skill[j+1] * i)

        return f[-1]

"""
now = max(now + skill[i-1] * x, f[i])
f[n-1] = now + skill[n-1] * x
[1,5,2,4] . [5,1,4,2]
[0,0,0,0]

now = 0, 
now = (0+5, 0) = 5
now = (5+25, 0) = 30
now = (30+10, 0) = 40
now = (40+20, 0) = 60

[5,30,40,60]
now = 5
now = (5+1, 30) = 30
now = (30+5, 40) = 40
now = (40+2, 60) = 60

[53,58,60,64]      [1,5,2,4]  [5,1,4,2]
now = 53
now = 53+4, 58 = 58
now = 58 + 20, 60 = 78
now = 78 + 8, 64 = 86

[102]



"""