class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []

        leds = [
            (8, 0), (4, 0), (2, 0), (1, 0),      
            (0, 32), (0, 16), (0, 8), (0, 4), (0, 2), (0, 1)  
        ]

        def walk(i, count, hour, minute):
            if count == turnedOn:
                ans.append(f"{hour}:{str(minute).zfill(2)}")
                return

            for i in range(i, len(leds)):
                h, m = leds[i]
                if (hour + h > 11) or (minute + m > 59):
                    continue
                walk(i + 1, count + 1, hour + h, minute + m)

        walk(0, 0, 0, 0)
        return ans