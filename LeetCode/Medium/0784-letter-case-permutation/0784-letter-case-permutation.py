class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = set()
        @cache
        def recurse(i, path):
            if i == len(s):
                res.add(path)
                return    
            if s[i].isalpha():
                recurse(i + 1, path + s[i].upper())
                recurse(i + 1, path + s[i].lower())
            else:
                recurse(i+1, path + s[i])
        recurse(0, "")
        return list(res)
        