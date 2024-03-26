#make table of 16
a=16*1
b=16*2
c=16*3
d=16*4
e=16*5
f=16*6
g=16*7
h=16*8
i=16*9
j=16*10
print(a,b,c,d,e,f,g,h,i,j)

#divisible by 7
k=16%7
l=32%7
m=48%7
n=64%7
o=80%7
p=96%7
q=112%7
r=128%7
s=144%7
t=160%7
print(k,l,m,n,o,p,q,r,s,t)


#20 tak cube
A=1**3
B=2**3
C=3**3
D=4**3
E=5**3
F=6**3
G=7**3
H=8**3
I=9**3
J=10**3
K=11**3
L=12**3
N=13**3
O=14**3
P=15**3
Q=16**3
R=17**3
S=18**3
T=19**3
U=20**3
print(A,B,C,D,E,F,G,H,I,J,K,L,N,O,P,Q,R,S,T,U)

#bitwise operator task
print('bitwise and')
print(22&12)
print(64&11)
print(13&9)
print(14&8)
print('bitwise or')
print(22|12)
print(64|11)
print(13|9)
print(14|8)
print('bitwise xor')
print(22^12)
print(64^11)
print(13^9)
print(14^8)







######## if else ladder task
            
percentage=30

if percentage>=80:
    print("A")  

elif percentage>=70:
    print("B")
elif percentage>=60:
    print("C")
elif percentage>=50:
    print("D")
elif percentage>=40:
    print("E")
else :
    print("fail")


print("sapceeeeeeeeeeeeeeeeeeeeeeeeeeeeee")


percentage=40

if percentage>=30:
    print("C")  
elif percentage>=40:
    print("B")
elif percentage>=50:
    print("A")
else :
    print("fail")
print("________________________________________________")



#looops
i=40
while i<=80:
    print(i)
    i+=1

e=995
while e>=655:
    print(e)
    e-=1

r=30
while r<=45:
    print(r)
    r+=1


print("spaceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")


I=0
while I<=10:
    print(I*2)
    I+=1








# amstrong number
 
gh=153
ans=0
while gh>9:
    eee=gh%10
    ans+=eee**3
    gh=gh//10
    print(eee)
ans+=gh**3
print(ans)


for uu in range(1,6):
    gggg=""
    for ii in range(5,-1):
        gggg+=str(ii)
        print(gggg)





















for y in range(1,5+1):
    aa=""
    for x in (" * * * * * * * ") :
      aa+=str(x)+" "
    print(aa)

for t in range(1,5+1):
    bb=""
    for r in (" * * * * * * ") :
      bb+=str(r)+" "
      print(bb)

 
for k in range (0,6 ):
    aaaaa=""
    for xx in range(6,k,-1):
        aaaaa=aaaaa+str(xx)+" "
    print(aaaaa)


for L  in range (1,5):
    aaaaaa=""
    for xxx in range(L,5):
        aaaaaa=aaaaaa+str(xxx)+" "
    print(aaaaaa)


for pp  in range (1,6):
    aaaaabb=""
    for xxy in (pp," * * * * * * ",):
        aaaaabb=aaaaabb+str(xxy)+" "
    print(aaaaabb)

        
for xuuuuuu in range(9):
    if (xuuuuuu==1):
        print(" * ")
    elif(xuuuuuu==2):
        print(" * * ")
    

