    def firstUniqChar(self, s: str) -> int:
        g=0
        for i in range(0,len(s)):
            f=0
            for j in range(0,len(s)):
                if(s[i]==s[j] and i!=j):
                    f=1
                    break
            if (f==0):
                g=1
                return(i)
                break
        if (g==0):
            return(-1)
