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

for pp  in range (1,6):
    aaaaabb=""
    for xxy in (" * * * * * * ",):
        aaaaabb=aaaaabb+str(xxy)+" "
    print(aaaaabb)

        
for xuuuuuu in range(9):
    if (xuuuuuu==1%9):
        print(" * ")
    elif(xuuuuuu==2%9):
        print(" * * ")

#print("______________________________________________") 
#u=int( input(" enter the number of rows"))
#o=int(input("enter the number of colums")) 
#b=""
#for i in range(1,u+1):
#    for p in range(1,o+1):
 #       b=b+("* ")
   # print(b)


















print("________________________________________________________")






f=""
for k in range(1,6):
    f=f+("* ")
    if (k==1 or k==5):
        print(" * * * * * * ")
       
  
    else:
        print( " *         * ")


print("__________________________________________________________________")


for e in range (0,6):
    if e==0 or e==5:
     bag=""
     for q in range (6):
       bag=bag+"* "
     print(bag)
    else:
      jhola=""
      for w in range (6):
       if w==0 or w==5:
           jhola=jhola+"* "
       else:
           jhola=jhola+"  "
      print(jhola) 

print("______________________________________")



for t in range(0,6):
   if t==0 or t==5:
     jhola=""
     for k in range (5+1):
         jhola=jhola+("* ")
     else:
       for u in range(6):
          if u==0 or u==5:
            jhola=jhola+("* ")
          elif u==[1,1]:
             jhola=jhola+("*")
          elif u==[2,2]:
             jhola=jhola+("*")
          elif u==(3,3):
             jhola=jhola+("*")
          elif u==[4,4]:
             jhola=jhola+("*")
          else:
             print("not applicable")
     print(jhola)


      
   
     
   


