mylist=[["a","b","c"]
       ,["d","e","f"]
       ,["g","h","i"]]

r=0
c=2
bag=""
while  c>=0:
    bag=bag+mylist[r][c]+" "
    c-=1
r=1
c=1
while r<=2:
    bag=bag+mylist[r][c]+" "
    r+=1
    c+=1
r=2
c=1
while c>=0:
    bag=bag+mylist[r][c]+" "
    c-=1
print(bag)

print("________________________________________________________________________-")


yourlist=[["a","b","c"]
         ,["d","e","f"]
         ,["g","h","i"]]

ro=0
co=0
jhola=""
while co<=2:
    jhola=jhola+yourlist[ro][co]+"  "
    co+=1
    ro+=1
ro=0
co=2
while ro<=2:
    jhola=jhola+yourlist[ro][co]+"  "
    co-=1
    ro+=1
print(jhola)
    
print("_____________________________________________________")

alllist=[["a","b","c"]
        ,["d","e","f"]
        ,["g","h","i"]]

rw=0
cw=0
container=""
while rw<=2:
    container=container+alllist[rw][cw]+"  "
    rw+=1


rw=2
cw=1
while cw<=2:
     container=container+alllist[rw][cw]+"  "
     cw+=1

rw=1
cw=2
while rw<=2:
    container=container+alllist[rw][cw]+"  "
   
    rw+=1
print(container)