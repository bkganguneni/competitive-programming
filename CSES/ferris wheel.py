# cook your dish here
n = list ( map ( int , input().split()))
w = list( map ( int, input().split()))
w.sort()

i =0
j= len(w)-1
count = 0
maxx= n[1]
while i <= j:
    if w[i] + w[j] > maxx:
        
        j -=1
    else:
        i +=1
        j -=1
    count = count +1

print(count)