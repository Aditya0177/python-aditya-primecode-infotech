#TUPLES AND ITS LENGHT
fruits=("apple","banana","cherry")
len_of_my_tupel=len(fruits)
print(fruits,len_of_my_tupel)

lisst=list(("my name"))
tupple=tuple(("this","is","typle","this","is","this","is","typle","this","is"))# to make it identify as tuple we have to put ,
print (type(lisst))
print(type(tupple))

print(tuple[0:-1])


footballer=("ronaldo,messi,neymarjr,haaland,mbappe")
if "ronaldo" in footballer :
    print("goat")
    if "ibrahmovich" not in footballer:
        print("goat ronaldo")



#how to add something in tuples as we cant ad in like lists
x=("apple","banana","cherry")
y= list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#add items
name=("aditya","anushka")
l=list(name)
l.append("priyanshu")
name=(l)
print(name)

q=("hhhhhhh")
p=("eeeeeee")
q+=p
print(q)

#delete 

W=("lol",)
del W


# unpack items in tupels after * everything will be in list


wwe=("johncena","undertaker","ajstyles","brocklesnar","johncena","undertaker","ajstyles","brocklesnar","cmpunk")
(tshirt,blackpants,gloves,*shorts)=wwe
print(tshirt)
print(blackpants)
print(gloves)
print(shorts)

#multiply
I=("asdjanjfnaf")
L=I*8
print(L)
