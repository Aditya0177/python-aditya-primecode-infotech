fruits={"tomato","mango","grapes","pineapple"}
vegetables=set(("spinach","brocoli","potato","cabbage"))
print(fruits)


fruits.add("peru")
print(fruits)
fruits.update(vegetables)

A={"viper","legion","rgb"}
B=("thinkpad","rgb")
C= A.union(B)
print(C)    
c=A.intersection(B)
print(C)

##################################### METHODS ###############################################################
#clear clears the whole set
q={"amma ki chu*t"}
q.clear()
print(q)

#copy copies the whole set
w={"dalal","america","ka"}
e={"america ka","tu"}
W=w.copy()
print(W)

#difference contains a set having difference
w.difference(e)
print(W)

#difference update changes the set
w.difference_update(e)
print()

#intersection update 
Inter={"hui","ohiuhuihuo","jhhhh"}
ghhh={"hui","jjhihihio","oihuohuhh"}
qqqqq=Inter.intersection_update(ghhh)
print(qqqqq)

#isdjoint returns ehther the two sets have an intersection or not
r={"kohli","gambhir","naveen ul haq"}
t={"shryas","pant","warner"}
R=r.isdisjoint(t)
print(R)

###################issubset returns wheter the set contains subset or not
u={"uuuuuu","uhhhhhhhh","jjjjjjjjjj","llllllllll"}
i={'jnnnnnnn','jjkkkkk','llllllllll'}
j=u.union(i)
U=u.issubset(i)
print(U)

#issuperset returs whther the set contains another superset or not
I=u.issuperset(i)
print(I)

#pop pops out an element from the set
O={"xhennai","supper","kings"}
O.pop()
print(O)

#remove removes any specific element
M=O.remove("supper")
print(M)

