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



        
        def dfs(s: str):

            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs('')

        return res