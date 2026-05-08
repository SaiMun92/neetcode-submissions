class Solution:
    def isPali(self, string):
        if string == string[::-1]:
            return True
        return False
        
    def dfs(self, i, res, part):
        # base case
        if i == len(self.s):
            res.append(list(part))
            return
        for j in range(i, len(self.s)):
            curr = self.s[i:j+1]
            
            if self.isPali(curr):
                part.append(curr)
                self.dfs(j+1, res, part)
                part.pop()


    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        self.s = s

        self.dfs(0, res, part)
        return res