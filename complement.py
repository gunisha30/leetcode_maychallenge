def findComplement(self, num: int) -> int:
        s=""
        while(num!=0):
            a = num % 2
            s = s + str(a)
            num=num//2
        s=s[::-1]
        l=list(s)
        print(l)
        for i in range(0,len(l)):
            if (l[i]=='0'):
                l[i]='1'
            else:
                l[i]='0'
        s="".join(l)
        return(int(s,2))
