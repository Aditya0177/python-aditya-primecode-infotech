#/n new line
a="my namae is \naditya"
print(a)

#/t tab
b="my name is\taditya"
print(b)

#/b backspace
c="cooler iss \bon"
print(c)

#/000 octal value
d="\101,\104'\111,\124,\131,\101"
print(d)

#/xhh hex values
e="\x41 \x44 \x49 \x54 \x59 \x41"
print(e)

#capitalize converts first letter in capital
f="wildcraft"
print(f.capitalize())

#casefold converts fist letter in small
g="Dildcraft"
print(g.casefold())

#center returns a center string
h="afajsifniajf"
print(h.center(20))

#count counts number of charecters 
i="adamfnonaifunuaifnuafuo"
print(i.count("a"))

#encode  returns encoded charecters are alpha numerical
j="1878915353"
print(j.encode())

#endswith tells that the string ends with the same charecter ir not
j="kalana"
print(j.endswith("a"))

#expandtabs sets tab sixe of string
k="   na  1hi batauga"
print(k.expandtabs())

#find finds charecter of the string
print(k.find("h"))

#isalnum returns true if all charecter in string are alpha numeric
l="12222234"
print(l.isalnum())

#isalpha returns true if all the charecters in string are numeric
m="afafafafaf"
print(m.isalpha())

#isacil returns true if all charecters are ascii
print(m.isascii())

#isadecimal if cahrecters are in decimal
print(m.isdecimal())

#isadogit if all cahrecters are digit
print(l.isdigit())

#isidentifier if string is identifier
print(m.isidentifier())

#islower all string charecters is in lower case
print(m.islower())

#isnumeric all charecters are numeric
print(l.isnumeric())

#isprintable if all charecters in string are printable
print(m.isprintable())

#isspace if charecters have whitespace
print(k.isspace())
#istitle turns capital of starting of each word
z="dawdatatatt"
print(z.istitle())
#isupper if all charecters have upperspace
n="END FOR TODAY"
print(n.isupper())                      