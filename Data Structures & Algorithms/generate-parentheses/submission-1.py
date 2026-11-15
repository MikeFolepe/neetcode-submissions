class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def isValid(chars: str) -> bool:
            open = 0
            for char in chars:
                open += 1 if char == '(' else - 1
                if open < 0:
                    return False 
            
            return open == 0



        
        def dfs(s: str, open: int, close: int):

            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return
            if open < n:
                dfs(s + '(', open + 1, close)
            if close < open:
                dfs(s + ')', open, close + 1)

        dfs('', 0, 0)

        return res