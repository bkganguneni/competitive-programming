
t = int(input())
while t>0:
    n = int(input())
    print(2**(len(bin(n).replace('0b',''))-1)-1)
            
    
    t = t-1