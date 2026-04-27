class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        hashmap = defaultdict(list)

        for i in range(len(code)):
            y =  True

            for j in code[i]:
                if not j.isalpha() and not j.isdigit() and not j == "_":
                    y = False
                    break

            if (businessLine[i] not in {"electronics", "grocery", "pharmacy", "restaurant"}) or not code[i] or not isActive[i]:
                y =  False

            if y:
                hashmap[businessLine[i]].append(code[i])

        for i in hashmap:
            hashmap[i].sort()

        return hashmap["electronics"] + hashmap["grocery"] + hashmap["pharmacy"] + hashmap["restaurant"]