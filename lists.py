cricketers=["gautam","mahendra singh","virat","yuvraj","rohit","jasprit","zaheer","ravichandran","ravindra","sachin"]

print(type(cricketers))

print(cricketers[0])

surname=list(("gambhir","dhoni","kohli","singh","sharma","bumrah","khan","ashwin","jadeja","tendulkar"))

print(surname[0])

print(cricketers[0]+" "+surname[0])
print(cricketers[1]+" "+surname[1])
print(cricketers[2]+" "+surname[2])
print(cricketers[3]+" "+surname[3])
print(cricketers[4]+" "+surname[4])
print(cricketers[5]+" "+surname[5])
print(cricketers[6]+" "+surname[6])
print(cricketers[7]+" "+surname[7])
print(cricketers[8]+" "+surname[8])
print(cricketers[9]+" "+surname[9])
cricketers[1]="suresh"
print(cricketers)
print(len(cricketers))



##################################      METHODS       ##############################################

agents=list(("reya","cypher","brimstone","jett"))
abilities=["flash","trip","smoke","updraft"]
#append adds an element at the end of the list
agents.append("reyna")
print(agents)
#insert inserts item in specified index
agents.insert(2,"astra")
print(agents)
#clear removes all the elements from the list
agents.clear()
print(agents)
#copy returns a ccopy of the list
agents.copy()
print(agents)
#count shows number odd elements in the value
agents.count(agents)
print(agents)
#extend adds two list in list 1
agents.extend(abilities)
print(agents)
#index reuturns index of first element with value
a=agents.index("reya")
print(a)
#pop removes the element 
agents.pop(1)
print(agents)
#remove removes the item with specified value
agents.remove("reya")
print(agents)
#reverse reverses the order of the list
agents.reverse()
print(agents)
#sort sorts the list according to namealphabets ascending
agents.sort()
print(agents)
# reverse sort descending alphabets
agents.sort(reverse=True)
print(agents)

#delete deletes the whole list
o=["chalna be"] 
del o