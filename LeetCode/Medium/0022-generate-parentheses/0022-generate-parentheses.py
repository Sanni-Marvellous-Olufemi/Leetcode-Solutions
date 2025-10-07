class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =  []

        @cache
        def walk(curr, opens, close):
            nonlocal n
        
            if opens > n or close > n or close > opens:
                return

            if len(curr) == n*2:
                ans.append(curr)
                return
            
            if opens < n:
                walk(curr+"(", opens+1, close)
                
            if close <= opens:
                walk(curr+")", opens, close+1)
                    
 
        walk("", 0, 0)
        return ans
            

            