import math
r=int(input())
k=r
p=0
X=[]
Y=[]
for i in range(-k+1,k):
    y= math.sqrt((r*r)-(i*i))
    ny=int(y)
    if(ny!=y):
        for b in range(-ny,ny+1):
            X.append (i)
            Y.append(b)
    if(ny==y):
        for c in range(-ny+1,ny):
            X.append(i)
            Y.append(c)
#for i in range(0,len(X)):
    #print(X[i],",",Y[i])
for n1 in range(0,len(X)):
    x0=0
    y0=0
    x1=X[n1]
    y1=Y[n1]
    if(x1==0 and y1==0):
        p=p
    else:
        for n2 in range (n1+1,len(X)):
            x2=X[n2]
            y2=Y[n2]
            if(x2==0 and y2==0):
                p=p
            else:
                for n3 in range (n2+1,len(X)):
                    x3=X[n3]
                    y3=Y[n3]
                    if(x3==0 and y3==0):
                        p=p
                    else:
                        if(x2-x1!=0):
                            a1=((y2-y1)/(x2-x1))*(x1)-y1
                        if(x2-x1==0):
                            a1=(1000000*(y2-y1)*(x1))-y1
                        if(x3-x2!=0):
                            a2=((y3-y2)/(x3-x2))*(x2)-y2
                        if(x3-x2==0):
                            a2=(1000000*(y3-y2)*(x2))-y2
                        if(x1-x3!=0):
                            a3=((y1-y3)/(x1-x3))*(x3)-y3
                        if(x1-x3==0):
                            a3=(1000000*(y1-y3)*(x3))-y3
                        
                        #print(x1,y1,"|",x2,y2,"|",x3,y3)
                        if(a1>0 and a2>0 and a3>0):
                            p=p+1
                        elif (a1<0 and a2<0 and a3<0):
                            p=p+1
                            #print("yes")
#print(len(X))
print(p)
    
