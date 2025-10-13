class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sets, memo = set(wordDict), {}

        def walk(index):
            nonlocal s

            if index in memo:
                return memo[index]

            for i in range(index, len(s)):
                if s[index:i] in sets:
                    ans = walk(i)
                    memo[i] = ans
                    if ans:
                        return True
                

            memo[index] = s[index:] in sets
            return memo[index]

        return walk(0)

"""
-Solve recursively using dfs, memoize and backtrack
-There are always 2 options at every index. If the index is the end of a word in worddict, pass in index + 1 to the recursive function (begining of a new word) or continue with the index until you find another index that is the end of a word.
e.g for "catsandog",  ["cats","dog","sand","and","cat"]
opt1 = t is treated as the end of a word in worddict (word = cat, new word starts from s)
opt2 = t is not treated as the end of a word, instead, t is just a normal leeter in a word (word = cats) and s is treated as the end of the word instead
-Opt1 is first recursively called, then if it returns false, we discard it and try the next option
-If it return True, no need to try out any other aption as all conditiond have been met so return True
-The main function would only contain a set of worddict and a memo to cache visited indices
-The recursive function takes in the starting index of a new word.
-In the recursive function, base case is if the index passed in is in memo, return memo[index]
-Recursive case is trying out opt1 and opt2. Use a for loop to iterate through the remaining indices in s, starting from the index passed in. In the for loop, if the index passed in sliced to the current index is a word in the set (s[index:i] in set), call the recursive function on the next index. Save the value of the recursive call as memo[i] and return true if the value is true
-If the value is False, discard the current word (s[index:i]) and keep iterating until you find another index that (s[index:i]) in sets, and rpeat the above steps on it.
-If you don't get a true recursive value after going through the for loop, check in index sliced to the end of the list (s[index:len(s)]) is in sets and save the answer to memo[index]
-Return the answer when you're done
-In the main function, call the recursive function on index 0 and return the answer
"""