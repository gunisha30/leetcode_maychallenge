def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l=coordinates
        f=0
        c=0
        n=len(coordinates)
        for i in range(0,n-1):
            if(l[i][0]==l[i+1][0]):
                c=1
                break
        if(c==0):
            
            slope = ( l[1][1] - l[0][1] ) / ( l[1][0] - l[0][0] )
            
            for i in range(2,n):
                
                slope1 = ( l[i][1] - l[0][1] ) / ( l[i][0] - l[0][0] )
                if(slope1!=slope):
                    f=1
                    break
            if(f==0):
                return (True)
            else:
                return (False)
        
        else:
            for i in range(1,n):
                if(l[i][0]!=l[0][0]):
                    f=1
                    break 
            if(f==0):
                return (True)
            else:
                return (False)
