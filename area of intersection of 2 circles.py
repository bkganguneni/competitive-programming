import math
class Solution:
    def intersectionArea(self,X1,Y1,R1,X2,Y2,R2):
        d = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
        if d > (R1+R2):
            return 0
        if d <= abs(R1-R2):
            return (3.14*(min(R1,R2)**2))
            
        alpha = math.acos((R1*R1+d*d-R2*R2)/(2*R1*d))*2
        beta = math.acos((R2*R2+d*d-R1*R1)/(2*R2*d))*2
        
        area1 = 0.5*alpha*R1*R1-0.5*R1*R1*math.sin(alpha)
        area2 = 0.5*beta*R2*R2-0.5*R2*R2*math.sin(beta)
        
        return  (area1+area2)
        
import math
        
if __name__=='__main__':
    X1=int(input())
    Y1 = int(input())
    R1 = int(input())
    X2=int(input())
    Y2 = int(input())
    R2 = int(input())
    ob=Solution()
    ans=ob.intersectionArea(X1,Y1,R1,X2,Y2,R2)
    print("{0:.6f}".format(ans))
