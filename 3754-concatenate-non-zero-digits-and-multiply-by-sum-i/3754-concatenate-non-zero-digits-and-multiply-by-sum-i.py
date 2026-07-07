class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n ==0:
            return 0
        k  = str(n)
        j = 0
        q = ""
        for  i in k:
            if int(i) != 0:
                j += int(i)
                q += i
        return int(q)*j
            

        